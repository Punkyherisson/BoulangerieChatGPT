# Recréation du fichier produits_pains.py après réinitialisation de l'environnement

pains_classiques = {
    "Baguette": {
        "ingredients": {
            "farine": 250,  # g
            "eau": 175,
            "levure": 5,
            "sel": 5
        },
        "cout": 0.40  # €
    },
    "Pain de campagne": {
        "ingredients": {
            "farine": 300,
            "eau": 210,
            "levure": 6,
            "sel": 6
        },
        "cout": 0.50
    },
    "Pain complet": {
        "ingredients": {
            "farine_complete": 300,
            "eau": 210,
            "levure": 6,
            "sel": 6
        },
        "cout": 0.55
    },
    "Pain aux céréales": {
        "ingredients": {
            "farine": 250,
            "eau": 180,
            "levure": 5,
            "sel": 5,
            "graines": 20
        },
        "cout": 0.60
    },
    "Pain de mie": {
        "ingredients": {
            "farine": 300,
            "eau": 180,
            "levure": 6,
            "sel": 6,
            "sucre": 10,
            "lait": 50,
            "beurre": 20
        },
        "cout": 0.65
    }
}

# Sauvegarde dans un fichier Python
fichier_produits_pains = '/mnt/data/produits_pains.py'
with open(fichier_produits_pains, 'w', encoding='utf-8') as f:
    f.write("pains_classiques = " + repr(pains_classiques))
