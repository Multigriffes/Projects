import requests
import os

plateform = input("La plateform")
player = input("Le joueur")
fp = open(player + plateform + ".txt", "w", encoding="utf-8", newline="\n")
url = ("https://api.mozambiquehe.re/bridge?auth=95f0efbc14fc27681790be9963d1b212&player=" + (player) + "&platform=" + (plateform) + "&enableClubsBeta=true&merge=true")
reponse_player = requests.get(url)

if reponse_player.status_code == 200:
    fp.write(reponse_player.text)
    print("Reponse written in a txt file")
elif reponse_player.status_code == 400:
    print("Try again in a few minute")
elif reponse_player.status_code == 403:
    print("Unauthorized / Unknown API key")
elif reponse_player.status_code == 404:
    print("The player could not be found")
elif reponse_player.status_code == 405:
    print("External API error")
elif reponse_player.status_code == 410:
    print("Unknown platform provided")
elif reponse_player.status_code == 429:
    print("Rate limit reached")
elif reponse_player.status_code == 500:
    print("Internal error")
else: 
    print("Unknow error")

fp.close()
input("Press enter to exit")
