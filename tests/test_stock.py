from stock import initialiser_stock, afficher_stock, fabriquer_pain
from produits_pains import recettes_pains_classiques

# Initialiser un stock de test
stock = initialiser_stock({
    "farine": 10000,       # en grammes
    "eau": 8000,
    "levure": 1000,
    "sel": 500,
})

print("\n📦 Stock initial :")
afficher_stock(stock)

# Choisir un pain classique à fabriquer
pain = "baguette"  # ou "pain de campagne", etc.
quantite = 10      # nombre d’unités à fabriquer

print(f"\n🛠️ Fabrication de {quantite} {pain}(s)")

# Lancer la fabrication
success = fabriquer_pain(stock, pain, quantite, recettes_pains_classiques)

if success:
    print("\n✅ Stock mis à jour après fabrication :")
    afficher_stock(stock)
else:
    print("\n❌ Stock insuffisant pour fabriquer ce pain.")

