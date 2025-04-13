# 🌍 EcoBrain v4.1 – IA augmentée pour la transition écologique

**EcoBrain** est une IA éthique et pédagogique conçue pour guider les citoyens, collectivités et entreprises vers des actions environnementales personnalisées et mesurables.

La version **4.1** intègre des modules intelligents, un score global environnemental (type NutriScore), un système d'historique comparatif et des outils d’exportation de rapport.

---

## 🧠 Fonctionnalités clés

- ✅ IA DQN simplifiée pour suggérer des actions personnalisées
- ✅ Score environnemental global de A à E basé sur 6 à 8 modules
- ✅ Modules thématiques : mobilité, eau, déchets, solaire, électroménager
- 📈 Historique des scores hebdomadaires + comparateur d’évolution
- 🗂 Mode simulation pour écoles, collectivités, ONG (sans données privées)
- 📦 Export PDF de son impact écologique
- 🎨 Interface visuelle avec bannière, logo et favicon personnalisables

---

## 📁 Structure du projet

ecobrain_v4.1/ │ ├── app.py ← Application principale Streamlit ├── modules/ ← Modules d’analyse par domaine │ ├── mobility.py │ └── scoring.py ├── utils/ ← Fonctions transversales │ ├── history_manager.py │ └── pdf_export.py ├── assets/ ← Favicon, logo, bannière │ ├── banner.html │ ├── logo.png │ └── favicon.ico ├── data/ ← Données régionales ou utilisateur simulées │ └── sample_data.json ├── requirements.txt ← Dépendances Python └── README.md ← Ce fichier

---

## 🚀 Lancer l’application en local

```bash
git clone https://github.com/ton_utilisateur/ecobrain_v4.1.git
cd ecobrain_v4.1
pip install -r requirements.txt
streamlit run app.py

