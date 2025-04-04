
from produits_pains import recettes_pains_classiques, recettes_pains_speciaux

# Stock initial en grammes
stock = {
    "farine": 50000,
    "eau": 30000,
    "levure": 2000,
    "sel": 1000,
    "beurre": 5000,
    "lait": 3000,
    "graines": 2000,
    "miel": 1000,
    "figues": 1000,
    "noix": 1000,
}

def initialiser_stock():
    """Réinitialise le stock avec des quantités par défaut."""
    global stock
    stock.update({
        "farine": 50000,
        "eau": 30000,
        "levure": 2000,
        "sel": 1000,
        "beurre": 5000,
        "lait": 3000,
        "graines": 2000,
        "miel": 1000,
        "figues": 1000,
        "noix": 1000,
    })

def afficher_stock():
    """Affiche les quantités actuelles en stock."""
    print("\n📦 Stock actuel :")
    for ingredient, quantite in stock.items():
        print(f" - {ingredient} : {quantite} g")

def ajouter_ingredient(ingredient, quantite):
    """Ajoute une quantité à un ingrédient du stock."""
    if ingredient in stock:
        stock[ingredient] += quantite
    else:
        stock[ingredient] = quantite

def verifier_disponibilite(nom_pain, quantite=1):
    """Vérifie si les ingrédients sont disponibles pour produire X pains."""
    recettes = recettes_pains_classiques | recettes_pains_speciaux
    recette = recettes.get(nom_pain)
    if not recette:
        print(f"⚠️ Pain inconnu : {nom_pain}")
        return False

    for ingr, qte in recette["ingredients"].items():
        if stock.get(ingr, 0) < qte * quantite:
            print(f"❌ Pas assez de {ingr} pour {quantite} {nom_pain}(s)")
            return False
    return True

def utiliser_ingredients(nom_pain, quantite=1):
    """Utilise les ingrédients pour fabriquer X pains."""
    if not verifier_disponibilite(nom_pain, quantite):
        return False

    recettes = recettes_pains_classiques | recettes_pains_speciaux
    recette = recettes[nom_pain]
    for ingr, qte in recette["ingredients"].items():
        stock[ingr] -= qte * quantite

    print(f"✅ {quantite} {nom_pain}(s) préparé(s) !")
    return True
