import boulangerie
import sauvegarde
import parametres_lieu

def afficher_recapitulatif(boutique, info_boulangerie):
    """Affiche un récapitulatif des choix effectués pour la boulangerie."""
    print("\n📌 Récapitulatif :")
    print(f"🏢 Boutique : {boutique}")
    print(f"📍 Lieu : {info_boulangerie['lieu']}")
    print(f"🛠 Mode : {info_boulangerie['mode']}")
    print(f"⚖️ Forme juridique : {info_boulangerie['forme_juridique']}")
    print(f"💰 Budget : {info_boulangerie['budget']} €")

def main():
    print("Bienvenue dans le jeu de création de boulangerie !")

    # Vérifier si un joueur existe déjà
    joueur = input("Entrez votre nom : ")
    boutiques = sauvegarde.rechercher_joueur(joueur)

    if boutiques:
        print(f"\nJoueur trouvé : {joueur}")
        print("Boulangeries existantes :")
        for i, nom in enumerate(boutiques, 1):
            print(f"{i}. {nom}")
        print("0. Créer une nouvelle boulangerie")

        choix = input("Choisissez une boulangerie à reprendre ou entrez 0 pour en créer une nouvelle : ")
        if choix.isdigit() and 1 <= int(choix) <= len(boutiques):
            boutique = boutiques[int(choix) - 1]
            info_boulangerie = sauvegarde.charger_sauvegarde(joueur, boutique)
            
            # ✅ Utilisation de la fonction d'affichage
            afficher_recapitulatif(boutique, info_boulangerie)
            lieu = info_boulangerie['lieu']
            params = parametres_lieu.obtenir_parametres_lieu(lieu)
            print(f"\n📍 {lieu} - Concurrence : {params['concurrence']['niveau']}")
            print(f"Loyer mensuel : {params['loyer_mensuel'][0]}€ à {params['loyer_mensuel'][1]}€")
            print(f"Taxes : CFE = {params['taxes'].get('CFE', 'N/A') * 100}%, CET = {params['taxes'].get('CET', 'N/A') * 100}%")

            return

    # Création d'une nouvelle boulangerie
    boutique, info_boulangerie = boulangerie.creation_boulangerie(joueur)
    sauvegarde.enregistrer_sauvegarde(joueur, boutique, info_boulangerie)

    # ✅ Utilisation de la fonction d'affichage
    afficher_recapitulatif(boutique, info_boulangerie)
    lieu = info_boulangerie['lieu']
    params = parametres_lieu.obtenir_parametres_lieu(lieu)
    print(f"\n📍 {lieu} - Concurrence : {params['concurrence']['niveau']}")
    print(f"Loyer mensuel : {params['loyer_mensuel'][0]}€ à {params['loyer_mensuel'][1]}€")
    print(f"Taxes : CFE = {params['taxes'].get('CFE', 'N/A') * 100}%, CET = {params['taxes'].get('CET', 'N/A') * 100}%")

if __name__ == "__main__":
    main()