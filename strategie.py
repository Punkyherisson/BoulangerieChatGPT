"""📌 1. Ajout des choix de gestion
🎯 Chaque mois, le joueur pourra choisir une stratégie qui aura un impact sur ses revenus et coûts.

Stratégie	Effet sur les clients	Effet sur les coûts
🔥 Promo spéciale (-10% prix)	+20% de clients	-10% sur le CA
🎭 Publicité locale (300€)	+15% de clients	-300€
⏳ Réduction des horaires	-10% de clients	-5% de frais de personnel
🥖 Hausse des prix (+10%)	-15% de clients	+10% sur le CA
🚀 Qualité premium (bio, artisanat)	+5% de clients fidèles	+5% sur les coûts de production
⚖️ Gestion neutre (aucun changement)	Aucun effet	Aucun effet"""

def choisir_strategie():
    """Permet au joueur de choisir une stratégie de gestion mensuelle."""
    strategies = {
        "1": {"nom": "🔥 Promo spéciale (-10% prix)", "effet_clients": +20, "effet_ca": -10, "effet_cout": 0},
        "2": {"nom": "🎭 Publicité locale (300€)", "effet_clients": +15, "effet_ca": 0, "effet_cout": -300},
        "3": {"nom": "⏳ Réduction des horaires", "effet_clients": -10, "effet_ca": 0, "effet_cout": -5},
        "4": {"nom": "🥖 Hausse des prix (+10%)", "effet_clients": -15, "effet_ca": +10, "effet_cout": 0},
        "5": {"nom": "🚀 Qualité premium (bio, artisanat)", "effet_clients": +5, "effet_ca": 0, "effet_cout": +5},
        "6": {"nom": "⚖️ Gestion neutre", "effet_clients": 0, "effet_ca": 0, "effet_cout": 0}
    }

    print("\n📌 Choisissez une stratégie de gestion pour ce mois :")
    for key, strat in strategies.items():
        print(f"{key}. {strat['nom']}")

    choix = input("Entrez le numéro de votre choix : ").strip()
    return strategies.get(choix, strategies["6"])  # Par défaut : gestion neutre
    