# parametres_lieu.py

import random

PARAMETRES_LIEU = {
    "Paris": {
        "loyer_mensuel": (5000, 12000),
        "taxes": {
            "CFE": 0.03,
            "CET": 0.03
        },
        "concurrence": {
            "niveau": "Forte",
            "perte_clients": 0.30
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