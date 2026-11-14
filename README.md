# Telecom-et-Reseaux
Projet telecom :routage optimal de paquets et placement de machines virtuelles dans le cloud
# APPLICATION D'OPTIMISATION : PLACEMENT DE MACHINES VIRTUELLES ET ROUTAGE OPTIMAL DE PAQUETS

## 1. Présentation du projet

Ce projet consiste à concevoir et développer une application web permettant de résoudre et de visualiser deux problèmes importants d'optimisation informatique :

- **Le placement optimal des machines virtuelles (VM)** sur un ensemble de serveurs physiques, en tenant compte des ressources disponibles et des contraintes de capacité.
- **Le routage optimal des paquets de données** dans un réseau informatique, avec pour objectif de minimiser la latence et la congestion tout en respectant les contraintes de capacité du réseau.

L'application réunira ces deux modules au sein d'une interface graphique moderne, interactive et accessible.

## 2. Objectifs du projet

### 2.1. Module de placement des machines virtuelles

- Implémenter et comparer plusieurs algorithmes de placement.
- Optimiser l'utilisation des ressources des serveurs.
- Respecter les contraintes de capacité.
- Mesurer les performances des différentes méthodes.
- Présenter les résultats sous forme de tableaux et de graphiques.

### 2.2. Module de routage optimal des paquets

- Étudier et exploiter une topologie de réseau informatique.
- Déterminer les chemins possibles entre les différents nœuds.
- Minimiser la latence et la congestion sous contrainte de capacité.
- Comparer les solutions de routage obtenues.
- Afficher les chemins et leurs pourcentages respectifs.
- Visualiser le déplacement des paquets dans le réseau.

### 2.3. Visualisation interactive

L'application devra proposer :
- Une représentation graphique du réseau.
- Une visualisation 3D des nœuds et des liaisons.
- Une animation du déplacement individuel des paquets.
- Des commandes de lecture, pause et réinitialisation.
- Des indicateurs de latence, de congestion et d'utilisation des ressources.

## 3. Technologies envisagées

- **Python** : langage principal.
- **Streamlit** : développement de l'interface web.
- **NetworkX** : manipulation et analyse des graphes.
- **Plotly** : visualisations interactives et 3D.
- **Pandas** : traitement et présentation des données.
- **PuLP** : résolution des problèmes d'optimisation linéaire.
- **Git et GitHub** : gestion du code source et collaboration.

Les bibliothèques définitives seront confirmées après l'analyse des programmes existants.

## 4. Organisation du projet

```text
application-optimisation/
│
├── app.py
├── requirements.txt
├── README.md
│
├── placement/
│   ├── __init__.py
│   ├── placement_vm-1.py
│   └── interface_placement.py
│
├── routage/
│   ├── __init__.py
│   ├── routage_africa-1.py
│   ├── africa.gml
│   ├── interface_routage.py
│   └── visualisation_3d.py
│
├── tests/
│
└── docs/
    └── missions_equipe.md
```

Cette structure pourra évoluer selon les besoins de l'intégration.

## 5. Répartition des responsabilités

Le projet est réalisé par une équipe de cinq membres.

### Membre 1 : Responsable du module de placement

**Branche :** `feature/placement`

Missions :
- Étudier le programme initial de placement.
- Identifier les fonctions et algorithmes existants.
- Développer l'interface utilisateur du module.
- Permettre la saisie et la génération des instances.
- Afficher les résultats des algorithmes.
- Réaliser des graphiques comparatifs sur l'utilisation des ressources.
- Visualisation graphique(La visualisation du placement devra permettre d'observer graphiquement la répartition des machines virtuelles sur les serveurs physiques ainsi que l'évolution de leurs capacités au cours du processus d'allocation.)

**Livrable attendu :** `placement/interface_placement.py`

### Membre 2 : Responsable du module de routage

**Branche :** `feature/routage`

Missions :
- Étudier le programme initial de routage.
- Exploiter la topologie `africa.gml`.
- Identifier les fonctions de calcul des chemins et d'évaluation.
- Développer l'interface utilisateur du module.
- Afficher les chemins obtenus et leurs pourcentages.
- Présenter les indicateurs de latence et de congestion.

**Livrable attendu :** `routage/interface_routage.py`

### Membre 3 : Responsable de la visualisation 3D

**Branche :** `feature/visualisation-3d`

Missions :
- Concevoir la représentation 3D du réseau.
- Afficher les nœuds et les connexions.
- Animer le déplacement individuel des paquets.
- Différencier visuellement les chemins empruntés.
- Ajouter les commandes de lecture, pause, réinitialisation et réglage de vitesse.
- Assurer la cohérence entre les résultats du routage et leur représentation graphique.

**Livrable attendu :** `routage/visualisation_3d.py`

### Membre 4 : Responsable des tests et de la documentation

**Branche :** `feature/tests`

Missions :
- Concevoir des instances de test pour le placement.
- Tester les différents algorithmes de placement.
- Concevoir des réseaux simples pour tester le routage.
- Vérifier le respect des contraintes.
- Identifier et signaler les erreurs.
- Rédiger les rapports de tests et la documentation technique.
- Participer à la validation finale de l'application.

**Livrables attendus :** fichiers de tests et documentation technique.

### Membre 5 : Responsable de l'architecture et de l'intégration

**Branche de travail principale :** `develop`

Missions :
- Définir l'architecture générale de l'application.
- Développer le point d'entrée `app.py`.
- Concevoir la page d'accueil et le système de navigation.
- Définir les interfaces entre les différents modules.
- Intégrer les travaux des autres membres.
- Vérifier le bon fonctionnement de l'application complète.
- Coordonner les validations et les corrections.

**Livrables attendus :** application intégrée et fonctionnelle.

## 6. Organisation du travail avec GitHub

Le projet utilise plusieurs branches afin de faciliter le travail collaboratif.

| Branche | Utilisation |
|---|---|
| `main` | Version stable du projet |
| `develop` | Intégration des fonctionnalités |
| `feature/placement` | Développement du placement |
| `feature/routage` | Développement du routage |
| `feature/visualisation-3d` | Visualisation 3D |
| `feature/tests` | Tests et documentation |

### Règles de collaboration

1. Chaque membre travaille sur sa branche dédiée.
2. Il est interdit de modifier directement la branche `main`.
3. Les programmes originaux doivent être conservés sans modification non validée.
4. Chaque nouvelle fonctionnalité doit être développée dans les fichiers qui lui sont attribués.
5. Les modifications sont proposées à travers une Pull Request vers `develop`.
6. Le responsable de l'intégration vérifie et valide les modifications avant leur fusion.
7. Toute erreur détectée doit être signalée et corrigée avant la validation finale.

## 7. Méthodologie de réalisation

Le développement suivra les étapes suivantes :

**Phase 1 : Analyse**
- Étude des programmes existants.
- Identification des fonctions réutilisables.
- Vérification des dépendances.

**Phase 2 : Développement des modules**
- Création de l'interface de placement.
- Création de l'interface de routage.
- Développement de la visualisation 3D.

**Phase 3 : Tests**
- Vérification individuelle des modules.
- Tests sur des instances simples.
- Vérification des contraintes et des résultats.

**Phase 4 : Intégration**
- Réunion des différents modules dans Streamlit.
- Mise en place de la navigation.
- Vérification de la communication entre les composants.

**Phase 5 : Validation finale**
- Tests complets de l'application.
- Correction des anomalies.
- Finalisation de la documentation.

## 8. Résultat final attendu

À la fin du projet, nous souhaitons obtenir une application web intégrée permettant :

- D'exécuter et de comparer plusieurs méthodes de placement de machines virtuelles.
- D'étudier et d'optimiser le routage des paquets dans un réseau.
- De visualiser les résultats numériques et graphiques.
- D'observer en 3D le déplacement des paquets.
- De consulter les indicateurs de performance et les contraintes respectées.

L'objectif est de proposer un outil pédagogique et technique permettant de mieux comprendre, expérimenter et comparer des méthodes d'optimisation appliquées aux infrastructures informatiques.

---

**Projet réalisé dans le cadre des travaux pratiques et projets informatiques de l'équipe.**
