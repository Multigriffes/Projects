import requests

plateform = input("La plateform")
player = input("Le joueur")
url = ("https://api.mozambiquehe.re/bridge?auth=95f0efbc14fc27681790be9963d1b212&player=" + (player) + "&platform=" + (plateform) + "&enableClubsBeta=true&merge=true")
reponse_player = requests.get(url)

if reponse_player.status_code == 200:
    print(reponse_player.text)

else:
    print("Error")

