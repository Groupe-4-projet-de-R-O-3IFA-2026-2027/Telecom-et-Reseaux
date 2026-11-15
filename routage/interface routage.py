
import sys
import copy
import importlib.util
from pathlib import Path

import streamlit as st
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


# Chemins des fichiers
DOSSIER = Path(__file__).resolve().parent
CHEMIN_CODE = DOSSIER / "routage_africa-1.py"
CHEMIN_GML = DOSSIER / "africa.gml"


# Chargement du programme de routage existant
@st.cache_resource
def charger_module():
    spec = importlib.util.spec_from_file_location(
        "routage_core", CHEMIN_CODE
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def afficher_interface():

    st.title("Routage optimal de paquets")
    st.write(
        "Minimisation de la latence et de la congestion "
        "sous contrainte de capacité."
    )

    try:
        core = charger_module()

        graphe = core.charger_graphe(str(CHEMIN_GML))

        # Construction de l'instance de routage
        instance_base = core.convertir_graphe_en_instance(graphe)
        core.simuler_capacites_et_delais(instance_base, graphe)

    except Exception as erreur:
        st.error(f"Erreur lors du chargement du réseau : {erreur}")
        return

    noeuds = sorted([str(n) for n in graphe.nodes()])

    st.subheader("1. Paramètres du réseau")

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox(
            "Routeur source",
            noeuds,
            index=noeuds.index("6272") if "6272" in noeuds else 0
        )

    with col2:
        destination = st.selectbox(
            "Routeur destination",
            noeuds,
            index=noeuds.index("6266") if "6266" in noeuds else min(1, len(noeuds)-1)
        )

    volume = st.number_input(
        "Volume de données à transmettre (Mb)",
        min_value=1.0,
        max_value=1000.0,
        value=20.0,
        step=5.0
    )

    st.subheader("2. Choix de la méthode")

    methode = st.selectbox(
        "Objectif du routage",
        [
            "Minimiser la latence",
            "Minimiser la congestion",
            "Somme pondérée",
            "Contrainte sur la congestion"
        ]
    )

    alpha = 0.5
    u_max = 0.20

    if methode == "Somme pondérée":
        alpha = st.slider(
            "Importance accordée à la latence",
            0.0, 1.0, 0.5, 0.05
        )

    if methode == "Contrainte sur la congestion":
        u_max = st.slider(
            "Congestion maximale autorisée",
            0.05, 1.0, 0.20, 0.05
        )

    if st.button("Lancer l'optimisation", type="primary"):

        if source == destination:
            st.warning("La source et la destination doivent être différentes.")
            return

        if not nx.has_path(graphe, source, destination):
            st.error("Aucun chemin ne relie ces deux routeurs.")
            return

        inst = copy.deepcopy(instance_base)
        inst.demandes = [(source, destination, float(volume))]
        inst.K = [0]
        inst.volume_total = float(volume)

        with st.spinner("Calcul du routage optimal..."):

            try:
                if methode == "Minimiser la latence":
                    resultat = core.resoudre_objectif(inst, "latence")

                elif methode == "Minimiser la congestion":
                    resultat = core.resoudre_objectif(inst, "congestion")

                elif methode == "Somme pondérée":
                    resultat_latence = core.resoudre_objectif(
                        inst, "latence"
                    )
                    resultat_congestion = core.resoudre_objectif(
                        inst, "congestion"
                    )

                    if resultat_latence[1] != "Optimal" or resultat_congestion[1] != "Optimal":
                        st.error("Impossible de calculer les deux solutions de référence.")
                        return

                    L_star = core.evaluer_routage(
                        inst, resultat_latence[0]
                    )["L"]

                    U_star = core.evaluer_routage(
                        inst, resultat_congestion[0]
                    )["U"]

                    resultat = core.somme_ponderee_routage(
                        inst, alpha, L_star, U_star
                    )

                else:
                    resultat = core.contrainte_sur_critere(inst, u_max)

                flots, statut = resultat[0], resultat[1]

                if statut != "Optimal":
                    st.error(f"Optimisation non concluante : {statut}")
                    return

                mesures = core.evaluer_routage(inst, flots)
                chemins = core.extraire_chemins(inst, flots)[0]

                st.success("Optimisation terminée avec succès.")

                st.subheader("3. Résultats")

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Latence moyenne",
                    f"{mesures['latence_moyenne']:.2f} ms"
                )

                c2.metric(
                    "Congestion maximale",
                    f"{mesures['U'] * 100:.2f} %"
                )

                c3.metric(
                    "Temps de calcul",
                    f"{resultat[2]:.3f} s"
                    if len(resultat) > 2 and isinstance(resultat[2], (int, float))
                    else "N/A"
                )

                st.subheader("4. Chemins empruntés")

                lignes = []

                for chemin, flot, fraction in chemins:
                    lignes.append({
                        "Chemin": " → ".join(map(str, chemin)),
                        "Volume transporté (Mb)": round(flot, 3),
                        "Pourcentage du trafic": round(fraction * 100, 2)
                    })

                if lignes:
                    tableau = pd.DataFrame(lignes)
                    st.dataframe(tableau, use_container_width=True)

                    st.subheader("5. Répartition du trafic")

                    fig, ax = plt.subplots()
                    ax.pie(
                        tableau["Pourcentage du trafic"],
                        labels=[
                            f"Chemin {i+1}"
                            for i in range(len(tableau))
                        ],
                        autopct="%1.1f%%",
                        startangle=90
                    )
                    ax.axis("equal")
                    st.pyplot(fig)
                    plt.close(fig)
                else:
                    st.warning("Aucun chemin n'a été extrait.")

                st.subheader("6. Vérification des contraintes")

                st.write(
                    "Liens dépassant 80 % de leur capacité :",
                    mesures["nb_liens_80"]
                )

                st.write(
                    "Liens dépassant leur capacité :",
                    mesures["nb_liens_depasses"]
                )

                st.write(
                    "Routage valide :",
                    "Oui" if mesures["valide"] else "Non"
                )

            except Exception as erreur:
                st.error(f"Une erreur est survenue : {erreur}")

