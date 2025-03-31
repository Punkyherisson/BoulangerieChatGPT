import boulangerie
import sauvegarde
import parametres_lieu
import couts

# 🔹 Version actuelle du programme
VERSION = "0.09"

def afficher_recapitulatif(joueur, boutique, info_boulangerie, params):
    """Affiche un récapitulatif détaillé de la boulangerie avec les coûts de fonctionnement."""
    
    print("\n📌 📊 RÉCAPITULATIF DE VOTRE BOULANGERIE 📊 📌")
    print("=" * 50)
    print(f"🏢 Nom de la boutique : {boutique}")
    print(f"👤 Gérant : {joueur}")
    print(f"📍 Lieu : {info_boulangerie['lieu']}")
    print(f"🛠 Mode : {info_boulangerie['mode']}")
    print(f"⚖️ Forme juridique : {info_boulangerie['forme_juridique']}")
    print(f"💰 Budget initial : {info_boulangerie['budget']} €")
    print("=" * 50)

    print("\n📊 🔹 Informations économiques :")
    print(f"💸 Loyer mensuel : {params['loyer_mensuel'][0]}€ - {params['loyer_mensuel'][1]}€")
    print(f"📊 Concurrence : {params['concurrence']['niveau']} (perte clients : {params['concurrence']['perte_clients']*100}%)")
    print(f"🛍️ Attentes clients - Qualité : {params['attentes_clients']['qualite']}/10, Prix max accepté : {params['attentes_clients']['prix_max']}/10")
    print(f"🚚 Livraison : {params['transport']['livraison']}/10, Accessibilité : {params['transport']['accessibilite']}/10")
    print(f"📜 Réglementation - Flexibilité : {params['reglementation']['flexibilite']}/10, Contraintes : {params['reglementation']['contraintes']}/10")
    print("=" * 50)

    # Récupération des tailles et du loyer pour le calcul des coûts
    taille_boutique = info_boulangerie["taille_boutique"]
    taille_labo = info_boulangerie["taille_labo"]
    loyer = params["loyer_mensuel"][1]  # Loyer haut de la fourchette
    resultats_couts = couts.calculer_cout_total(taille_boutique, taille_labo, info_boulangerie['lieu'], loyer)

    print("\n📉 💰 COÛTS DE FONCTIONNEMENT 💰 📉")
    for categorie, montant in resultats_couts["details"].items():
        print(f"🔹 {categorie.capitalize()} : {montant} €")
    print(f"\n💰 **Total des coûts mensuels : {resultats_couts['total']} €**")
    print("=" * 50)

def main():
    print(f"Bienvenue dans le jeu de création de boulangerie ! (Version {VERSION})")

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

            # ✅ Définition correcte de `params`
            lieu = info_boulangerie['lieu']
            params = parametres_lieu.obtenir_parametres_lieu(lieu)

            # ✅ Affichage complet du récapitulatif
            afficher_recapitulatif(joueur, boutique, info_boulangerie, params)
            return

    # Création d'une nouvelle boulangerie
    boutique, info_boulangerie = boulangerie.creation_boulangerie(joueur)
    sauvegarde.enregistrer_sauvegarde(joueur, boutique, info_boulangerie)

    # ✅ Définition correcte de `params`
    lieu = info_boulangerie['lieu']
    params = parametres_lieu.obtenir_parametres_lieu(lieu)

    # ✅ Affichage complet du récapitulatif
    afficher_recapitulatif(joueur, boutique, info_boulangerie, params)

if __name__ == "__main__":
    main()