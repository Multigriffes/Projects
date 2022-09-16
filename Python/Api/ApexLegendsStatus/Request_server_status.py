import requests
import os

fp = open("Current server status.json", "w", encoding="utf-8", newline="\n")
url = ("https://api.mozambiquehe.re/servers?auth=95f0efbc14fc27681790be9963d1b212")
reponse_server_status = requests.get(url)

if reponse_server_status.status_code == 200:
    fp.write(reponse_server_status.text)
    print("Reponse written in a json file")
elif reponse_server_status.status_code == 400:
    fp.write("Try again in a few minute")
    print("Try again in a few minute")
elif reponse_server_status.status_code == 403:
    fp.write("Unauthorized / Unknown API key")
    print("Unauthorized / Unknown API key")
elif reponse_server_status.status_code == 404:
    fp.write("The player could not be found")
    print("The player could not be found")
elif reponse_server_status.status_code == 405:
    fp.write("External API error")
    print("External API error")
elif reponse_server_status.status_code == 410:
    fp.write("Unknown platform provided")
    print("Unknown platform provided")
elif reponse_server_status.status_code == 429:
    fp.write("Rate limit reached")
    print("Rate limit reached")
elif reponse_server_status.status_code == 500:
    fp.write("Internal error")
    print("Internal error")
else: 
    fp.write("Unknow error")
    print("Unknow error")

fp.close()

input("Press enter to exit")