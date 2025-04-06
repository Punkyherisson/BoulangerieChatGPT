# === Recettes simplifiées pour test ===
recettes_pains_classiques = {
    "baguette": {
        "farine": 300,
        "eau": 200,
        "levure": 10,
        "sel": 5,
    },
    "pain de campagne": {
        "farine": 400,
        "eau": 300,
        "levure": 10,
        "sel": 5,
    }
}

# === Fonctions de stock ===
def initialiser_stock(quantites):
    return dict(quantites)

def afficher_stock(stock):
    print("📊 Stock actuel :")
    for ingredient, quantite in stock.items():
        print(f"  - {ingredient} : {quantite} g")

def fabriquer_pain(stock, nom_pain, quantite, recettes):
    if nom_pain not in recettes:
        print("⚠️ Recette inconnue.")
        return False

    recette = recettes[nom_pain]
    # Vérification du stock
    for ingr, qtt in recette.items():
        if stock.get(ingr, 0) < qtt * quantite:
            print(f"❌ Pas assez de {ingr}")
            return False

    # Mise à jour du stock
    for ingr, qtt in recette.items():
        stock[ingr] -= qtt * quantite

    print(f"✅ {quantite} {nom_pain}(s) fabriqué(s)")
    return True

# === Test ===
if __name__ == "__main__":
    stock = initialiser_stock({
        "farine": 5000,
        "eau": 4000,
        "levure": 500,
        "sel": 200,
    })

    afficher_stock(stock)
    print("\n🛠️ Fabrication de 10 baguettes :")
    fabriquer_pain(stock, "baguette", 10, recettes_pains_classiques)
    afficher_stock(stock)