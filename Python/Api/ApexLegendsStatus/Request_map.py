import requests

url = ("https://api.mozambiquehe.re/maprotation?auth=95f0efbc14fc27681790be9963d1b212")

reponse_map_code = requests.get(url)
reponse_map_text = requests.get(url)
print (reponse_map_code)
if reponse_map_code.status_code == 200:
    print(reponse_map_text.text)
else:
    print("Error")