# 🥖 Simulation de Boulangerie  

Un jeu de simulation textuel où vous gérez votre propre boulangerie-pâtisserie ! Prenez les bonnes décisions pour assurer la rentabilité et la croissance de votre commerce.  

## 📌 Introduction  
Dans ce jeu, vous ouvrez une boulangerie et devez gérer :  
✔️ L’implantation (Paris, ville moyenne, campagne)  
✔️ Les finances et les investissements  
✔️ La gestion du personnel et du recrutement  
✔️ Les stratégies commerciales  
✔️ L’impact des saisons et des événements aléatoires  

Objectif 🎯 : Maximiser les profits avant la fin de la période de simulation.  

---

## 🚀 Installation  

### ✅ **Prérequis**  
- Python 3.10+  
- Bibliothèques standard Python (`random`, `json`, etc.)  

### 📥 **Cloner le projet**  
```sh
git clone https://github.com/Punkyherisson/BoulangerieChatGPT.git
cd BoulangerieChatGPT

▶️ Lancer le jeu
python main.py

🎮 Utilisation
Au début de la partie, le joueur doit :
1️⃣ Choisir un nom de boulangerie
2️⃣ Sélectionner le lieu d’implantation
3️⃣ Déterminer la taille du magasin et du laboratoire
4️⃣ Définir une stratégie de gestion chaque mois
5️⃣ Gérer le personnel, la concurrence et la saisonnalité

Chaque mois, plusieurs éléments influencent les ventes :
🔹 Saisonnalité : Affluence variable selon les mois
🔹 Événements aléatoires : Grèves, pannes, canicules, etc.
🔹 Stratégies de gestion : Promotions, publicité, qualité premium

🏗️ Modules et Explications
📌 main.py – Lancement du jeu, gestion des sauvegardes.
📌 boulangerie.py – Création d’une nouvelle boutique.
📌 sauvegarde.py – Chargement/enregistrement des parties.
📌 parametres_lieu.py – Gestion des paramètres en fonction du lieu.
📌 couts.py – Calcul des coûts de fonctionnement.
📌 saisonnalite.py – Gestion de l’affluence mensuelle.
📌 strategie.py – Recrutement, gestion et stratégies mensuelles.

🔮 Évolutions prévues
✔️ Ajout d’un système d’événements aléatoires (grèves, fêtes, météo)
✔️ Intégration d’un système de réputation influençant la clientèle
✔️ Possibilité de diversifier les produits vendus en boutique
✔️ Interface graphique pour une meilleure immersion
