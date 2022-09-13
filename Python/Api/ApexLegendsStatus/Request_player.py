import requests

plateform = input("La plateform")
player = input("Le joueur")

url = requests.get ("https://api.mozambiquehe.re/bridge?auth=95f0efbc14fc27681790be9963d1b212&player=$player&platform=$plateform&enableClubsBeta=true&merge=true")

print = (url.status_code)

if url.status_code == 200:
    print(url.text)
else:
    print("Error")

