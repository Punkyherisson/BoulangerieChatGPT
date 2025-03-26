def choix_lieu():
    lieux = {"1": "Paris", "2": "Ville", "3": "Village à la campagne"}
    print("Choisissez un lieu d'implantation :")
    for key, value in lieux.items():
        print(f"{key}. {value}")
    choix = input("Entrez le numéro correspondant : ")
    return lieux.get(choix, "Ville")

def choix_forme_juridique():
    formes = {
        "1": "Entreprise Individuelle (EI)",
        "2": "SARL",
        "3": "SAS",
        "4": "SASU",
        "5": "SCOP"
    }
    print("\n📌 Formes juridiques disponibles :")
    for key, value in formes.items():
        print(f"{key}. {value}")
    choix = input("Entrez le numéro correspondant : ")
    return formes.get(choix, "EI")

def creation_boulangerie(joueur):
    boutique = input("Entrez le nom de votre boutique : ")
    lieu = choix_lieu()
    mode = input("Souhaitez-vous créer (C) ou reprendre (R) une boulangerie ? ").upper()
    forme_juridique = choix_forme_juridique()

    # Définition du budget de départ
    budget = {"apport": 20000, "emprunt": 0, "total": 20000}

    if mode == "R":
        cout_fond = {"Paris": 180000, "Ville": 120000, "Village à la campagne": 70000}
        rachat_fond = cout_fond[lieu]
        budget["emprunt"] = max(0, rachat_fond - budget["total"])
        budget["total"] += budget["emprunt"]

    return boutique, {
        "lieu": lieu,
        "mode": "Reprise" if mode == "R" else "Création",
        "forme_juridique": forme_juridique,
        "budget": budget
    }
