# 🌍 EcoBrain v4.1 – Intelligence Artificielle pour la transition écologique

**EcoBrain v4.1** est un prototype de cerveau planétaire numérique, guidé par une IA transparente, éthique et éducative.  
Il propose des **conseils personnalisés pour réduire votre impact environnemental**, visualiser vos progrès et simuler des scénarios collectifs.

---

## 🧠 Fonctionnalités clés

- ✅ **Suggestions IA contextuelles** via un agent DQN
- 📊 **Score écologique global** (type NutriScore de A à E)
- 🧩 **Modules spécialisés** : mobilité, eau, déchets, énergie solaire, électroménagers…
- 📈 **Historique et comparaison** des efforts hebdomadaires
- 🗂 **Mode simulation** pour collectivités, écoles, quartiers
- 📦 **Export PDF** de votre rapport environnemental
- 🎨 **Interface visuelle** avec bannière, logo et navigation claire

---

## 🧱 Structure du projet

ecobrain_v4.1/ ├── app.py ← Interface principale Streamlit ├── requirements.txt ← Dépendances Python │ ├── modules/ ← Analyse par thème │ ├── mobility.py │ └── scoring.py │ ├── utils/ ← Historique & PDF │ ├── history_manager.py │ └── pdf_export.py │ ├── assets/ ← Logo, favicon, bannière HTML │ ├── banner.html │ ├── logo.png │ └── favicon.ico │ └── data/ ← Données régionales ou simulées └── sample_data.json


---

## 🚀 Lancement local

1. Cloner le dépôt :
```bash
git clone https://github.com/ton_utilisateur/ecobrain_v4.1.git
cd ecobrain_v4.1

    Installer les dépendances :

pip install -r requirements.txt

    Lancer l’app :

streamlit run app.py

---


📊 Mode simulation pédagogique

    Idéal pour des enseignants, mairies, collectivités territoriales ou étudiants.

    Aucune donnée personnelle requise

    Simule un comportement moyen pour une région ou une population

    Permet de tester différents scénarios d’action collective

🖨 Export PDF de votre rapport écologique

    Score global

    Modules notés

    Historique et évolution

    Format facile à imprimer ou partager (PDF ou CSV)

🔮 Roadmap prochaine version (v4.2)

    🔁 Connexion API open data (énergie, transport réel)

    📡 Dashboard collaboratif (niveau quartier / ville)

    🧠 Amélioration DQN + apprentissage long terme

    🏆 Gamification éthique et collaborative

🙌 Auteurs

Projet open source initié par Lemamm
Contributions bienvenues !
📄 Licence

MIT — Libre d'utilisation à des fins éducatives, citoyennes ou scientifiques.
