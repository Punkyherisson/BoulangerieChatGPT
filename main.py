import json
import os

FICHIER_SAUVEGARDE = "joueurs.json"

def charger_sauvegardes():
    """Charge toutes les sauvegardes existantes depuis le fichier JSON."""
    if os.path.exists(FICHIER_SAUVEGARDE):
        with open(FICHIER_SAUVEGARDE, "r") as f:
            return json.load(f)
    return []

def sauvegarder_partie(data):
    """Ajoute ou met à jour une sauvegarde dans le fichier JSON."""
    sauvegardes = charger_sauvegardes()
    
    # Vérifier si la sauvegarde existe déjà (même joueur et même boutique)
    for sauvegarde in sauvegardes:
        if sauvegarde["joueur"] == data["joueur"] and sauvegarde["boutique"] == data["boutique"]:
            sauvegarde.update(data)  # Met à jour les informations
            break
    else:
        sauvegardes.append(data)  # Ajoute une nouvelle sauvegarde
    
    # Sauvegarde dans le fichier JSON
    with open(FICHIER_SAUVEGARDE, "w") as f:
        json.dump(sauvegardes, f, indent=4)

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

def charger_partie():
    """Permet de charger une sauvegarde existante si elle existe."""
    sauvegardes = charger_sauvegardes()
    if not sauvegardes:
        print("Aucune sauvegarde trouvée.")
        return None

    print("Sauvegardes disponibles :")
    for i, sauvegarde in enumerate(sauvegardes, 1):
        print(f"{i}. {sauvegarde['joueur']} - {sauvegarde['boutique']} ({sauvegarde['lieu']})")

    choix = input("Entrez le numéro de la partie à charger (ou appuyez sur Entrée pour créer une nouvelle) : ")
    
    if choix.isdigit() and 1 <= int(choix) <= len(sauvegardes):
        return sauvegardes[int(choix) - 1]
    
    print("Nouvelle partie commencée.")
    return None

def main():
    print("Bienvenue dans le jeu de création de boulangerie !")
    
    # Tente de charger une partie existante
    data_existante = charger_partie()
    if data_existante:
        data = data_existante
    else:
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
        
        sauvegarder_partie(data)
        print("Données enregistrées avec succès !")
    
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
    