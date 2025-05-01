def obtenir_couts_fixes(taille_boutique, taille_stock, taille_vente):
    """Retourne les coûts fixes mensuels en fonction de la taille des espaces."""
    
    assurances_boutique = {
        "petite": 100,
        "moyenne": 150,
        "grande": 200
    }

    charges_stock = {
        "petite": 50,
        "moyenne": 80,
        "grande": 120
    }

    charges_vente = {
        "petite": 70,
        "moyenne": 110,
        "grande": 160
    }

    frais_bancaires = 50  # 🏦 Abonnement TPE fixe

    return {
        "assurances": assurances_boutique.get(taille_boutique, 150),
        "stock": charges_stock.get(taille_stock, 80),
        "vente": charges_vente.get(taille_vente, 110),
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


def calculer_cout_total(taille_boutique, taille_labo, taille_stock, taille_vente, lieu, loyer):
    """Calcule le coût total mensuel en intégrant le loyer du lieu."""
    couts_fixes = obtenir_couts_fixes(taille_boutique, taille_stock, taille_vente)
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