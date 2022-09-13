import requests

plateform = input("La plateform")
player = input("Le joueur")
reponse_player = requests.get("https://api.mozambiquehe.re/bridge?auth=95f0efbc14fc27681790be9963d1b212&player=" + (player) + "&platform=" + (plateform) + "&enableClubsBeta=true&merge=true")

if reponse_player.status_code == 200:
    print(reponse_player.text)
    reponse = reponse_player.text
else:
    print("Error")

    