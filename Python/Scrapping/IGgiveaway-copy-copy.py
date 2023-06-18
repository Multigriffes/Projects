import itertools
import requests

base_url = "https://www.instant-gaming.com/fr/giveaway/"

# Caractères possibles
caracteres_possibles = "pixa"

# Génération de toutes les combinaisons possibles
combinaisons = itertools.product(caracteres_possibles, repeat=5)

# Parcourir et afficher les URLs générées
for combinaison in combinaisons:
    url = base_url + "".join(combinaison)
    response = requests.get(url)
    if response.status_code == 200:
        print(url)
