# patisseries_arabes.py

recettes_patisseries_arabes = {
    "Makrout": {
        "ingredients": {
            "semoule": 200,
            "dattes": 100,
            "miel": 100,
            "beurre": 50
        },
        "cout_unitaire": 3.5
    },
    "Baklava": {
        "ingredients": {
            "pâte filo": 150,
            "amandes": 100,
            "miel": 100,
            "beurre": 80
        },
        "cout_unitaire": 4.5
    },
    "Cornes de gazelle": {
        "ingredients": {
            "farine": 150,
            "amandes": 100,
            "eau de fleur d'oranger": 50,
            "sucre": 50,
            "beurre": 40
        },
        "cout_unitaire": 3.8
    }
}

def verifier_stock(stock, recette):
    for ingredient, quantite in recette.items():
        if stock.get(ingredient, 0) < quantite:
            return False, ingredient
    return True, None

def fabriquer_produit(nom, stock, recettes=recettes_patisseries_arabes):
    if nom not in recettes:
        return f"❌ Recette inconnue : {nom}"
    
    recette = recettes[nom]["ingredients"]
    disponible, ingredient_manquant = verifier_stock(stock, recette)

    if not disponible:
        return f"❌ Stock insuffisant pour fabriquer {nom} : manque de {ingredient_manquant}."

    for ingredient, quantite in recette.items():
        stock[ingredient] -= quantite

    cout = recettes[nom]["cout_unitaire"]
    return f"✅ {nom} fabriqué avec succès. Coût : {cout:.2f} €"