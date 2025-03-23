import json

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
    print("Choisissez une forme juridique :")
    for key, value in formes.items():
        print(f"{key}. {value}")
    choix = input("Entrez le numéro correspondant : ")
    return formes.get(choix, "EI")

def main():
    print("Bienvenue dans le jeu de création de boulangerie !")
    joueur = input("Entrez votre nom : ")
    boutique = input("Entrez le nom de votre boutique : ")
    lieu = choix_lieu()
    mode = input("Souhaitez-vous créer (C) ou reprendre (R) une boulangerie ? ").upper()
    forme_juridique = choix_forme_juridique()
    
    budget = {"apport": 20000, "emprunt": 0, "total": 20000}
    if mode == "R":
        rachat_fond = int(input("Entrez le coût du fonds de commerce (en €) : "))
        emprunt = max(0, rachat_fond - budget["total"])
        budget["emprunt"] = emprunt
        budget["total"] += emprunt
    
    data = {
        "joueur": joueur,
        "boutique": boutique,
        "lieu": lieu,
        "mode": "Reprise" if mode == "R" else "Création",
        "forme_juridique": forme_juridique,
        "budget": budget
    }
    
    with open("joueur.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print("Données enregistrées avec succès !")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
