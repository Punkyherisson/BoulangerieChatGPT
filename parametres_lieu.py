# parametres_lieu.py

import random

PARAMETRES_LIEU = {
    "Paris": {
        "loyer_mensuel": (5000, 12000),
        "taxes": {
            "CFE": 0.03,  # 3%
            "CET": 0.03   # 3%
        },
        "concurrence": {
            "niveau": "Forte",
            "perte_clients": 0.3  # 30% des clients potentiels perdus
        },
        "attentes_clients": {
            "qualite": 9,  # Exigence sur la qualité (1 à 10)
            "prix_max": 7  # Sensibilité au prix (1 = bas prix, 10 = prix élevés acceptés)
        },
        "fournisseurs": {
            "choix": 10,  # Facilité d'accès aux fournisseurs (1 à 10)
            "cout": 8  # Coût des matières premières (1 = faible, 10 = très élevé)
        },
        "emplois": {
            "disponibilite": 9,  # Facilité de recrutement (1 à 10)
            "salaires": 10  # Niveau des salaires (1 = bas, 10 = très élevé)
        },
        "transport": {
            "accessibilite": 10,  # Facilité pour attirer les clients (1 à 10)
            "livraison": 4  # Besoin en véhicules de livraison (1 = faible, 10 = très élevé)
        },
        "reglementation": {
            "flexibilite": 4,  # Facilité des horaires et réglementations (1 = très contraignant, 10 = très souple)
            "contraintes": 8  # Niveau des restrictions légales (1 = faible, 10 = très strict)
        }
    },
    "Ville": {
        "loyer_mensuel": (2000, 5000),
        "taxes": {
            "CFE": 0.02,
            "CET": 0.02
        },
        "concurrence": {
            "niveau": "Moyenne",
            "perte_clients": 0.15
        },
        "attentes_clients": {
            "qualite": 7,
            "prix_max": 6
        },
        "fournisseurs": {
            "choix": 7,
            "cout": 6
        },
        "emplois": {
            "disponibilite": 6,
            "salaires": 7
        },
        "transport": {
            "accessibilite": 7,
            "livraison": 5
        },
        "reglementation": {
            "flexibilite": 6,
            "contraintes": 6
        }
    },
    "Village à la campagne": {
        "loyer_mensuel": (500, 2000),
        "taxes": {
            "CFE": 0.005,
            "exonérations": "Possibles pour revitalisation économique"
        },
        "concurrence": {
            "niveau": "Faible",
            "perte_clients": 0.05
        },
        "attentes_clients": {
            "qualite": 5,
            "prix_max": 9
        },
        "fournisseurs": {
            "choix": 4,
            "cout": 4
        },
        "emplois": {
            "disponibilite": 3,
            "salaires": 4
        },
        "transport": {
            "accessibilite": 3,
            "livraison": 8
        },
        "reglementation": {
            "flexibilite": 9,
            "contraintes": 2
        }
    }
}

def obtenir_parametres_lieu(lieu):
    """Retourne les paramètres d'un lieu donné."""
    return PARAMETRES_LIEU.get(lieu, {})

def calculer_clients_journaliers(lieu):
    """Calcule le nombre de clients en fonction du lieu et de la concurrence."""
    params = obtenir_parametres_lieu(lieu)
    
    base_clients = {
        "Paris": random.randint(150, 300),
        "Ville": random.randint(80, 150),
        "Village à la campagne": random.randint(30, 80)
    }

    clients_potentiels = base_clients.get(lieu, 0)

    # Application de la concurrence
    perte = params.get("concurrence", {}).get("perte_clients", 0)
    clients_reels = int(clients_potentiels * (1 - perte))

    print(f"📍 {lieu} : {clients_potentiels} clients potentiels, "
          f"mais concurrence {params.get('concurrence', {}).get('niveau', 'Inconnue')} "
          f"➝ {clients_reels} clients réels.")
    
    return clients_reels

# Test rapide du module
if __name__ == "__main__":
    for lieu in PARAMETRES_LIEU.keys():
        print(f"\n📍 Paramètres pour {lieu}:")
        print(obtenir_parametres_lieu(lieu))
        calculer_clients_journaliers(lieu)