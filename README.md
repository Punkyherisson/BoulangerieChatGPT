# 🥖 BoulangerieChatGPT

Bienvenue dans **BoulangerieChatGPT** : un jeu de simulation textuel qui vous plonge dans la gestion complète d’une boulangerie artisanale !  
📍 Choisissez votre lieu d’implantation, gérez vos stocks, fabriquez vos produits, recrutez votre équipe et faites prospérer votre entreprise !

---

## 🚀 Fonctionnalités principales

- 🌍 **Choix du lieu** : Paris, ville moyenne ou village – chaque environnement impacte les coûts, les clients et la concurrence.
- 🧑‍🍳 **Création ou reprise de boutique** : démarrez de zéro ou rachetez un fonds de commerce.
- 📊 **Paramètres économiques** : loyer, taxes, stock, surface de vente, budget initial, emprunt bancaire.
- 👥 **Gestion du personnel** : embauchez des employés selon votre spécialité (pâtisserie ou boulangerie).
- 📆 **Décisions mensuelles** :
  - Choix stratégiques (promo, pub, hausse des prix…)
  - Saisonnalité et événements aléatoires (pluie, grève, fête locale…)
- 🍞 **Fabrication et vente** :
  - Pains classiques et spéciaux
  - Viennoiseries
  - Pâtisseries françaises et orientales
  - Petite restauration (sandwichs, cafés…)
- 📦 **Système de gestion des stocks** avec calculs de coût de production
- 💾 **Sauvegardes multiples** et reprise de partie
- 🧪 **Tests unitaires** (à venir)

---

## 🗂️ Structure du projet
BoulangerieChatGPT/
 │ ├── core/ # Logique centrale du jeu 
 │ ├── jeu.py
 │ ├── gestion_jeu.py
 │ └── affichage.py 
 │ ├── data/ # Recettes et produits
 │ ├── produits_pains.py
 │ ├── produits_viennoiseries.py
 │ ├── produits_patisseries.py
 │ ├── produits_arabes.py
 │ └── petite_restauration.py
 │ ├── modules/ # Mécaniques et logique métier
 │ ├── parametres_lieu.py
 │ ├── saisonnalite.py
 │ ├── evenements.py
 │ ├── strategie.py
 │ ├── stock.py
 │ └── sauvegarde.py
 │ ├── utils/ # Utilitaires et constantes
 │ ├── fichiers.py │ ├── validations.py │ └── constantes.py │ ├── sauvegardes.json # Fichier de sauvegarde des parties ├── main.py # Point d’entrée du jeu
 ├── README.md # Ce fichier
 └── CHANGELOG.md # Journal des versions
 
 ## ⚙️ Lancer le jeu

1. Installe Python 3.10+  
2. Clone le dépôt :

git clone https://github.com/Punkyherisson/BoulangerieChatGPT.git
cd BoulangerieChatGPT
python main.py

💡 Objectif pédagogique
Ce projet est aussi un terrain d'apprentissage :

Python 🐍

Gestion de projet 🗂️

Git & GitHub 🧠

Organisation modulaire 🧱

Simulation et logique économique 📊

🧑‍💻 Auteur
Développé avec passion par @Punkyherisson

📜 Licence
Ce projet est libre de droits pour apprentissage et usage personnel.
Pas de commercialisation sans autorisation.