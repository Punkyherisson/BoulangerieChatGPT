import json

def charger_sauvegarde():
    """ Charge les sauvegardes existantes depuis joueurs.json """
    try:
        with open("joueurs.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def sauvegarder_joueurs(joueurs):
    """ Sauvegarde les données mises à jour dans joueurs.json """
    with open("joueurs.json", "w") as f:
        json.dump(joueurs, f, indent=4)

def choix_lieu():
    lieux = {"1": "Paris", "2": "Ville", "3": "Village à la campagne"}
    print("\n📍 Choisissez un lieu d'implantation :")
    for key, value in lieux.items():
        print(f"{key}. {value}")
    choix = input("Entrez le numéro correspondant : ").strip()
    return lieux.get(choix, "Ville")

def afficher_choix_forme_juridique():
    """ Affiche les formes juridiques et demande un choix """
    formes = {
        "1": "Entreprise Individuelle (EI) - Simplicité, mais responsabilité illimitée.",
        "2": "SARL - Structure sécurisée avec responsabilité limitée.",
        "3": "SAS - Flexibilité, adaptée aux projets évolutifs.",
        "4": "SASU - Variante de la SAS pour un entrepreneur seul.",
        "5": "SCOP - Société coopérative, idéale pour un projet collectif."
    }
    print("\n📜 **CHOIX DE LA FORME JURIDIQUE** 📜")
    for key, desc in formes.items():
        print(f"{key}. {desc}")
    
    choix = input("Entrez le numéro correspondant : ").strip()
    formes_sans_desc = {k: v.split(" - ")[0] for k, v in formes.items()}  # Récupérer juste les noms
    return formes_sans_desc.get(choix, "Entreprise Individuelle (EI)")

def get_achat_fond(lieu):
    """ Renvoie un coût moyen par défaut pour un rachat de fonds de commerce """
    couts = {"Paris": 250000, "Ville": 150000, "Village à la campagne": 80000}
    return couts.get(lieu, 150000)

def main():
    print("\n🏪 Bienvenue dans le jeu de création de boulangerie !")

    joueurs = charger_sauvegarde()
    
    # Demande du nom du joueur
    joueur = input("\n👤 Entrez votre nom : ").strip()

    # Vérification des sauvegardes existantes pour ce joueur
    boulangeries_existantes = [save["boutique"] for save in joueurs if save["joueur"] == joueur]

    if boulangeries_existantes:
        print(f"\n📂 Sauvegardes existantes pour {joueur} :")
        for i, b in enumerate(boulangeries_existantes, start=1):
            print(f"{i}. {b}")
        
        choix = input("\n🔄 Voulez-vous charger une sauvegarde existante ? (Oui/Non) ").strip().lower()
        if choix == "oui":
            num_sauvegarde = input("\n📌 Entrez le numéro de la boulangerie à charger : ").strip()
            if num_sauvegarde.isdigit():
                num_sauvegarde = int(num_sauvegarde) - 1
                if 0 <= num_sauvegarde < len(boulangeries_existantes):
                    boutique = boulangeries_existantes[num_sauvegarde]
                    sauvegarde = next((save for save in joueurs if save["joueur"] == joueur and save["boutique"] == boutique), None)
                    print("\n✅ Chargement réussi ! Voici les détails :")
                    print(json.dumps(sauvegarde, indent=4))
                    return  # Quitte la fonction après chargement de la partie
    
    # Création d'une nouvelle sauvegarde
    boutique = input("\n🏪 Entrez le nom de votre boutique : ").strip()
    lieu = choix_lieu()

    print("\n📢 Avant de continuer, choisissez la forme juridique de votre entreprise !")
    forme_juridique = afficher_choix_forme_juridique()

    mode = input("\n⚖️ Souhaitez-vous créer (C) ou reprendre (R) une boulangerie ? ").upper().strip()
    
    budget = {"apport": 20000, "emprunt": 0, "total": 20000}

    if mode == "R":
        valeur_defaut = get_achat_fond(lieu)
        rachat_fond_str = input(f"\n💰 Entrez le coût du fonds de commerce (en €) [Valeur par défaut : {valeur_defaut}] : ").strip()
        rachat_fond = int(rachat_fond_str) if rachat_fond_str else valeur_defaut  
        emprunt = max(0, rachat_fond - budget["total"])
        budget["emprunt"] = emprunt
        budget["total"] += emprunt
    else:
        coûts_démarrage = {"Paris": 50000, "Ville": 30000, "Village à la campagne": 20000}
        budget["total"] += coûts_démarrage.get(lieu, 30000)

    data = {
        "joueur": joueur,
        "boutique": boutique,
        "lieu": lieu,
        "mode": "Reprise" if mode == "R" else "Création",
        "forme_juridique": forme_juridique,
        "budget": budget
    }

    # Mise à jour ou ajout des nouvelles données
    for save in joueurs:
        if save["joueur"] == joueur and save["boutique"] == boutique:
            save.update(data)
            break
    else:
        joueurs.append(data)

    sauvegarder_joueurs(joueurs)

    print("\n✅ **Données enregistrées avec succès !**")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()