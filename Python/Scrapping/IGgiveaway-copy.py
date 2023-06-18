import itertools
import requests
from bs4 import BeautifulSoup
from termcolor import colored

base_url = "https://www.instant-gaming.com/fr/giveaway/"

# Liste des caractères possibles
caracteres_possibles = "abcdefghijklmnopqrstuvwxyz1234567890"

# Générer toutes les combinaisons de 5 caractères
combinaisons = itertools.product(caracteres_possibles, repeat=5)

# Parcourir toutes les combinaisons et vérifier les URLs correspondantes
for combinaison in combinaisons:
    url = base_url + "".join(combinaison)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    ligne_121 = soup.find_all('body')[0].find_all('p')[120].get_text()

    if "404" not in ligne_121:
        print(colored(url, 'green'))
    else:
        print(url)
