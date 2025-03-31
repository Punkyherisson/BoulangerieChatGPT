import json
import os

FICHIER_SAUVEGARDE = "joueurs.json"

def charger_donnees():
    """Charge les données du fichier JSON, ou retourne un dictionnaire vide si le fichier n'existe pas ou est invalide."""
    if os.path.exists(FICHIER_SAUVEGARDE):
        with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if isinstance(data, dict):  # Vérifie que c'est bien un dictionnaire
                    return data
                else:
                    print("❌ Erreur : Format JSON invalide. Réinitialisation...")
                    return {}
            except json.JSONDecodeError:
                print("❌ Erreur : Fichier JSON corrompu. Réinitialisation...")
                return {}
    return {}

def enregistrer_donnees(data):
    """Enregistre les données dans le fichier JSON."""
    with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def rechercher_joueur(joueur):
    """Renvoie la liste des boutiques enregistrées pour un joueur donné."""
    data = charger_donnees()
    return list(data.get(joueur, {}).keys())

def charger_sauvegarde(joueur, boutique):
    """Charge les informations d'une sauvegarde spécifique et ajoute les valeurs manquantes si nécessaire."""
    data = charger_donnees()
    info = data.get(joueur, {}).get(boutique, {})

    # Valeurs par défaut pour éviter les KeyError
    cles_defaut = {
        "taille_boutique": "moyenne",
        "taille_labo": "moyen",
        "taille_stock": "moyen",
        "taille_vente": "moyen"
    }

    modifie = False  # Vérifier si des changements sont faits

    for cle, valeur in cles_defaut.items():
        if cle not in info:
            info[cle] = valeur
            modifie = True

    # Mettre à jour et sauvegarder seulement si des modifications ont été apportées
    if modifie:
        enregistrer_sauvegarde(joueur, boutique, info)

    return info

def enregistrer_sauvegarde(joueur, boutique, info):
    """Enregistre ou met à jour la sauvegarde d'un joueur pour une boutique donnée."""
    data = charger_donnees()
    
    if joueur not in data:
        data[joueur] = {}
    
    data[joueur][boutique] = info
    enregistrer_donnees(data)
    
    print("\n✅ Sauvegarde réussie !")