import itertools
import requests

base_url = "https://www.instant-gaming.com/fr/giveaway/"

# Liste des caractères possibles
caracteres_possibles = "abcdefghijklmnopqrstuvwxyz1234567890"

# Générer toutes les combinaisons de 5 caractères
combinaisons = itertools.product(caracteres_possibles, repeat=5)

# Parcourir toutes les combinaisons et vérifier les URLs correspondantes
for combinaison in combinaisons:
    url = base_url + "".join(combinaison)
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        lines = content.splitlines()
        if len(lines) >= 121 and "404" not in lines[120]:
            print(url)
