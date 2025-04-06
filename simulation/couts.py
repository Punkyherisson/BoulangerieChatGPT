def obtenir_couts_fixes(taille_boutique):
    """Retourne les coûts fixes mensuels en fonction de la taille de la boutique."""
    assurances = {
        "petite": 100,  # Moins de matériel à couvrir
        "moyenne": 150,  # Standard
        "grande": 200  # Plus d'équipements, plus de risques
    }

    frais_bancaires = 50  # 🏦 Abonnement TPE fixe

    return {
        "assurances": assurances.get(taille_boutique, 150),
        "frais_bancaires": frais_bancaires,
    }

def obtenir_couts_variables(taille_labo, lieu):
    """Retourne les coûts variables mensuels selon la taille du labo et le lieu."""
    energie = {
        "petit": 400,
        "moyen": 600,
        "grand": 900
    }

    marketing = {
        "Paris": 500,
        "Ville": 300,
        "Village": 100
    }

    return {
        "electricite": energie.get(taille_labo, 600),
        "eau": 50,
        "gaz": 100,
        "marketing": marketing.get(lieu, 200),
    }

def calculer_cout_total(taille_boutique, taille_labo, lieu, loyer):
    """Calcule le coût total mensuel en intégrant le loyer du lieu."""
    couts_fixes = obtenir_couts_fixes(taille_boutique)
    couts_variables = obtenir_couts_variables(taille_labo, lieu)

    total = loyer + sum(couts_fixes.values()) + sum(couts_variables.values())

    return {
        "total": total,
        "details": {"loyer": loyer, **couts_fixes, **couts_variables}
    }

# Test rapide
if __name__ == "__main__":
    resultats = calculer_cout_total("moyenne", "moyen", "Ville", 1800)
    print("💰 Coût total mensuel :", resultats["total"], "€")
    print("📊 Détails des coûts :", resultats["details"])