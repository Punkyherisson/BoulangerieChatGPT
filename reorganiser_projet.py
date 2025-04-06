import os
import shutil

# Dossiers à créer
structure = {
    "data": [
   
        "viennoiserie.py",

    ],
    "simulation": [
        "couts.py",
        "saisonnalite.py",
        "evenements.py",
        "strategie.py",
        "stock2.py",
        "production.py",
    ],
    "utils": [
        "affichage.py",
        "json_utils.py",
        "calculs.py"
    ],
    "tests": ["test_stock.py", "stock_test.py", "test_patisseries.py"],
}

# Crée les dossiers s'ils n'existent pas
for dossier in structure:
    os.makedirs(dossier, exist_ok=True)

# Déplace les fichiers dans les bons dossiers
for dossier, fichiers in structure.items():
    for fichier in fichiers:
        if os.path.exists(fichier):
            print(f"📁 Déplacement de {fichier} ➝ {dossier}/")
            shutil.move(fichier, os.path.join(dossier, fichier))
        else:
            print(f"⚠️  Fichier {fichier} non trouvé, vérifie son nom.")

# Optionnel : créer un dossier tests vide pour plus tard
os.makedirs("tests", exist_ok=True)

print("\n✅ Réorganisation terminée ! Tu peux maintenant tester que tout fonctionne.")