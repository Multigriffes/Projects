import linecache
import requests
import os
to_delete = '  <!----><mini-song-card object="$ctrl.hit.result" ng-switch-when="song" search-highlights="$ctrl.hit.highlights"><a ng-href="'
heu = 1

while heu > 0 :
    song = input("What song name")
    url = ("https://genius.com/search?q="  + (song))
    reponse_search = requests.get(url)
    cache = open("cache.json", mode="w", encoding="utf-8", newline="\n")
    cache.write(reponse_search.text)
    read = linecache.getline("cache.json", 768)
    new_read = read.replace(to_delete,"")
    print(new_read)
    input("Press enter to another one")