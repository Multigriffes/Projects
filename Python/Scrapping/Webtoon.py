import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.webtoons.com/fr/fantasy/gold-forest/list?title_no=3448"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}

def download_episode(url, episode_number):
  # Téléchargez la page HTML
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, 'html.parser')

  # Récupérez le lien de téléchargement de l'épisode
  download_link = soup.find('img', {'class': '_images'})['src']

  # Téléchargez l'épisode
  response = requests.get(download_link)
  open(f'episode{episode_number}.jpg', 'wb').write(response.content)

# Téléchargez la page HTML de la liste des épisodes
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Récupérez la liste des épisodes
episode_list = soup.find_all('a', {'class': 'episode'})

# Parcourez chaque épisode de la liste et téléchargez-le
for i, episode in enumerate(episode_list):
  episode_url = episode['href']
  download_episode(episode_url, i+1)
