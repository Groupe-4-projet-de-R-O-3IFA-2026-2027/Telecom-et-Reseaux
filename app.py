from routage.interface_routage import afficher_interface
import streamlit as st
from pathlib import Path

# ============================================================
# TELECOM — INTERFACE PRINCIPALE
# Lancement : python -m streamlit run app.py
# ============================================================

st.set_page_config(
    page_title="Telecom | Network & Cloud",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

ROOT = Path(__file__).resolve().parent

# Couleurs
NAVY = "#10233F"
BLUE = "#246BCE"
GREEN = "#18A66A"
BG = "#F4F7FB"
TEXT = "#172B4D"
MUTED = "#6B7A90"

# ============================================================
# STYLE
# ============================================================

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'DM Sans', sans-serif;
    }}

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #10233F, #173D68);
    }}

    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    .brand {{
        display:flex;
        align-items:center;
        gap:12px;
        padding:8px 4px 22px;
    }}

    .brand-icon {{
        width:46px;
        height:46px;
        border-radius:14px;
        display:flex;
        align-items:center;
        justify-content:center;
        background:linear-gradient(135deg,#38BDF8,#246BCE);
        font-size:24px;
    }}

    .brand-name {{
        font-size:23px;
        font-weight:800;
        color:white;
    }}

    .brand-sub {{
        font-size:10px;
        color:#BBD2EC;
        letter-spacing:2px;
        text-transform:uppercase;
    }}

    .hero {{
        background:linear-gradient(115deg,#10233F,#174C82,#246BCE);
        border-radius:22px;
        padding:34px;
        color:white;
        margin-bottom:24px;
    }}

    .hero h1 {{
        color:white;
        font-size:34px;
    }}

    .hero p {{
        color:#D8E9FB;
        max-width:650px;
        line-height:1.7;
    }}

    .section-title {{
        font-size:21px;
        font-weight:800;
        color:{NAVY};
        margin:15px 0 5px;
    }}

    .section-sub {{
        font-size:13px;
        color:{MUTED};
        margin-bottom:18px;
    }}

    .module-card {{
        background:white;
        border:1px solid #E5EBF3;
        border-radius:18px;
        padding:22px;
        min-height:200px;
    }}

    .module-card h3 {{
        color:{NAVY};
        font-size:18px;
    }}

    .module-card p {{
        color:{MUTED};
        font-size:13px;
        line-height:1.6;
    }}

    .page-head {{
        background:white;
        border:1px solid #E5EBF3;
        border-radius:17px;
        padding:21px 24px;
        margin-bottom:20px;
    }}

    .page-head h1 {{
        color:{NAVY};
        font-size:25px;
    }}

    .page-head p {{
        color:{MUTED};
        font-size:13px;
    }}

    .info-box {{
        border-radius:13px;
        background:#EAF3FF;
        border-left:4px solid {BLUE};
        padding:14px 16px;
        color:#284B75;
        font-size:13px;
        line-height:1.6;
    }}

    .stButton > button {{
        border:0;
        border-radius:10px;
        padding:.62rem 1rem;
        font-weight:700;
        background:{GREEN};
        color:white;
    }}

    .stButton > button:hover {{
        background:#128655;
        color:white;
    }}

    .footer {{
        margin-top:40px;
        padding:16px 0;
        border-top:1px solid #E2E9F2;
        color:#8290A3;
        font-size:11px;
        text-align:center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# NAVIGATION
# ============================================================

PAGES = [
    "Accueil",
    "Routage de paquets",
    "Placement Cloud"
]

if "telecom_page" not in st.session_state:
    st.session_state.telecom_page = "Accueil"

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🌐</div>
            <div>
                <div class="brand-name">Telecom</div>
                <div class="brand-sub">Network & Cloud tools</div>
            </div>
        </div>
        <p style="font-size:11px;letter-spacing:1px;">
            NAVIGATION PRINCIPALE
        </p>
        """,
        unsafe_allow_html=True
    )

    selected = st.radio(
        "Navigation",
        PAGES,
        index=PAGES.index(st.session_state.telecom_page),
        label_visibility="collapsed"
    )

    st.session_state.telecom_page = selected

    st.markdown(
        """
        <div style="
            margin-top:28px;
            padding:14px;
            border-radius:13px;
            background:rgba(255,255,255,.08);
            font-size:12px;
            line-height:1.6;">
            <b>Plateforme Telecom</b><br>
            Une interface unique pour expérimenter
            le routage optimal et le placement Cloud.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="margin-top:22px;font-size:10px;">Develop by Penseur™ Software</p>',
        unsafe_allow_html=True
    )

# ============================================================
# FONCTIONS D'AFFICHAGE
# ============================================================

def page_header(title, subtitle, icon):

    st.markdown(
        f"""
        <div class="page-head">
            <div style="font-size:25px;">{icon}</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def source_tab(candidate_files):

    # Recherche du fichier dans son dossier respectif
    existing = next(
        (ROOT / name for name in candidate_files
         if (ROOT / name).is_file()),
        None
    )

    if existing:

        st.caption(
            f"Fichier chargé : {existing.relative_to(ROOT)}"
        )

        code = existing.read_text(
            encoding="utf-8",
            errors="replace"
        )

        st.code(code, language="python")

    else:

        st.info(
            "Le fichier source de ce module n'a pas encore été ajouté. "
            "Il apparaîtra ici après son intégration dans le projet."
        )


def render_module_page(
    title,
    subtitle,
    icon,
    source_files,
    integration_name
):

    page_header(title, subtitle, icon)

    run_tab, code_tab = st.tabs(
        ["▶ Exécuter", "</> Code source"]
    )

    with run_tab:

        st.markdown(
            f"""
            <div class="info-box">
                <b>Zone du module {integration_name}</b><br>
                L'interface générale est prête.
                Le programme métier sera connecté ici
                dès que son fichier sera intégré au projet.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")
        st.markdown("**Espace de travail**")

        st.caption(
            "Les paramètres, résultats et visualisations "
            "apparaîtront ici après l'intégration de l'algorithme."
        )

    with code_tab:

        source_tab(source_files)


# ============================================================
# PAGE D'ACCUEIL
# ============================================================

if st.session_state.telecom_page == "Accueil":

    st.markdown(
        '<p style="color:#246BCE;font-weight:bold;letter-spacing:2px;">PLATEFORME DE SIMULATION</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero">
            <h1>Bienvenue sur Telecom</h1>
            <p>
                Une plateforme pour analyser les réseaux,
                optimiser le transfert des paquets et organiser
                intelligemment les ressources Cloud.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Explorer les modules</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-sub">Choisissez le module à utiliser.</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:

        st.markdown(
            """
            <div class="module-card">
                <div style="font-size:30px;">🛰️</div>
                <h3>Routage optimal de paquets</h3>
                <p>
                    Étudier les chemins possibles dans un réseau
                    et comparer différentes méthodes de routage.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Ouvrir le module de routage",
            use_container_width=True
        ):
            st.session_state.telecom_page = "Routage de paquets"
            st.rerun()

    with c2:

        st.markdown(
            """
            <div class="module-card">
                <div style="font-size:30px;">☁️</div>
                <h3>Placement de serveurs Cloud</h3>
                <p>
                    Explorer les stratégies de placement des
                    machines virtuelles et l'utilisation des serveurs.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Ouvrir le module Cloud",
            use_container_width=True
        ):
            st.session_state.telecom_page = "Placement Cloud"
            st.rerun()

    st.write("")

    st.markdown(
        '<div class="section-title">Vue d’ensemble</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3 = st.columns(3)

    m1.metric("Modules disponibles", "02")
    m2.metric("Interface", "Streamlit")
    m3.metric("Projet", "Telecom")


# ============================================================
# MODULE ROUTAGE
# ============================================================

elif st.session_state.telecom_page == "Routage de paquets":
    from routage.interface_routage import afficher_interface
    afficher_interface()

    render_module_page(
        "Routage optimal de paquets",
        "Analyse et comparaison des méthodes de routage dans un réseau.",
        "🛰️",
        [
            "routage/routage_africa-1.py",
            "routage/routage_africa.py",
            "routage/routage.py"
        ],
        "Routage"
    )


# ============================================================
# MODULE PLACEMENT
# ============================================================

elif st.session_state.telecom_page == "Placement Cloud":

    render_module_page(
        "Placement de serveurs Cloud",
        "Organisation des machines virtuelles et optimisation des ressources serveur.",
        "☁️",
        [
            "placement/placement_vm-1.py",
            "placement/code_placement.py",
            "placement/placement.py"
        ],
        "Placement Cloud"
    )


# ============================================================
# PIED DE PAGE
# ============================================================

st.markdown(
    """
    <div class="footer">
        TELECOM · Network & Cloud tools · Develop by Penseur™ Software
    </div>
    """,
    unsafe_allow_html=True
)

