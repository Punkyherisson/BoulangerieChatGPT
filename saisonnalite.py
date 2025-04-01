import datetime

def effet_saisonnalite():
    """Renvoie un multiplicateur en fonction du mois actuel pour ajuster la fréquentation des clients."""
    mois = datetime.datetime.now().month

    effets = {
        1: 0.90,  # Janvier (-10%)
        2: 0.95,  # Février (-5%)
        3: 1.00,  # Mars (stable)
        4: 1.05,  # Avril (+5%)
        5: 1.10,  # Mai (+10%)
        6: 1.15,  # Juin (+15%)
        7: 1.10,  # Juillet (+10%)
        8: 0.90,  # Août (-10%)
        9: 1.05,  # Septembre (+5%)
        10: 1.00, # Octobre (stable)
        11: 0.95, # Novembre (-5%)
        12: 1.20  # Décembre (+20%)
    }

    multiplicateur = effets.get(mois, 1.00)  # Par défaut, pas de modification
    print(f"📆 Mois actuel : {mois} ➝ Multiplicateur saisonnier : {multiplicateur:.2f}")

    return multiplicateur