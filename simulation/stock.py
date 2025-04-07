# stock.py

# Stock initial en grammes ou unités
stock = {
    "farine": 100_000,
    "eau": 100_000,
    "levure": 5_000,
    "sel": 2_000,
    "sucre": 3_000,
    "lait": 5_000,
    "beurre": 5_000,
    "noix": 2_000,
    "figues": 2_000,
    "olives": 2_000,
    "graines": 2_000,
    "farine de maïs": 2_000,
    "farine de châtaigne": 2_000
}
def verifier_stock(ingredients, recette, quantite): 
    """Vérifie si le stock permet de produire un certain nombre de pains."""
    for ingredient, qte_necessaire in recette["ingredients"].items():
        total_requis = qte_necessaire * quantite
        if ingredients.get(ingredient, 0) < total_requis:
            print(f"🚫 Pas assez de {ingredient} pour produire {quantite} {recette['nom']}")
            return False
    return True

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

def peut_produire(pain, quantite, recettes):
    """Vérifie si le stock permet de produire un certain nombre de pains."""
    if pain not in recettes:
        print(f"❌ Recette pour {pain} introuvable.")
        return False

    recette = recettes[pain]["ingredients"]

    for ingredient, qte_necessaire in recette.items():
        total_requis = qte_necessaire * quantite
        if stock.get(ingredient, 0) < total_requis:
            print(f"🚫 Pas assez de {ingredient} pour produire {quantite} {pain}")
            return False
    return True

def produire(pain, quantite, recettes):
    """Produit des pains et déduit les ingrédients du stock."""
    if not peut_produire(pain, quantite, recettes):
        return False

    recette = recettes[pain]["ingredients"]
    for ingredient, qte in recette.items():
        stock[ingredient] -= qte * quantite

    print(f"✅ {quantite} {pain} produit(s). Stock mis à jour.")
    return True

def reapprovisionner(ingredient, quantite):
    """Ajoute des ingrédients au stock."""
    if ingredient in stock:
        stock[ingredient] += quantite
    else:
        stock[ingredient] = quantite
    print(f"📦 +{quantite}g de {ingredient} ajouté au stock.")
from produits_pains import recettes_pains_classiques, recettes_pains_speciaux


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
