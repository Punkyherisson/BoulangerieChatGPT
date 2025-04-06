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
