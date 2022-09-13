import requests

url = ("https://api.mozambiquehe.re/maprotation?auth=95f0efbc14fc27681790be9963d1b212")

reponse_map = requests.get(url)

if reponse_map.status_code == 200:
    print(reponse_map.text)
else:
    print("Error")