import json
import pandas as pd

with open("joueurs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []
for joueur, boulangeries in data.items():
    for nom_boulangerie, infos in boulangeries.items():
        rows.append({
            "joueur": joueur,
            "boulangerie": nom_boulangerie,
            "lieu": infos.get("lieu", ""),
            "mode": infos.get("mode", ""),
            "forme_juridique": infos.get("forme_juridique", ""),
            "apport": infos.get("budget", {}).get("apport", 0),
            "emprunt": infos.get("budget", {}).get("emprunt", 0),
            "budget_total": infos.get("budget", {}).get("total", 0),
            "taille_boutique": infos.get("taille_boutique", ""),
            "taille_labo": infos.get("taille_labo", ""),
            "taille_stock": infos.get("taille_stock", ""),
            "taille_vente": infos.get("taille_vente", "")
        })

df = pd.DataFrame(rows)
df.to_excel("sauvegardes_boulangeries.xlsx", index=False)