import requests
import json
import urllib
from googlesearch import search

zoekterm = 'Kobus Bijker'
woonplaats = 'Winsum'
werkgever = 'Hanzehogeschool'

#zoekterm = input('Naam persoon: ')
#woonplaats = input('Woonplaats (?=niet weten of op zoeken): ')
#werkgever = input('Werkgever/School (?=niet weten of op zoeken): ')

exactname = '['+zoekterm+']'
results_EN = search(zoekterm, lang='english', num=10, stop=10,)
Res_Alg = []
for url in results_EN:
    if not 'crdev' in url: Res_Alg.append(url)
    #print(url)

results_NL = search(exactname, lang='dutch', num=10, stop=10,)
Res_NL = []
for url in results_NL:
    if url not in Res_Alg:
        Res_NL.append(url)
        if not 'crdev' in url: Res_Alg.append(url)
        #print(url)

zoekterm2 = exactname +' AND '+ woonplaats
results_WP = search(zoekterm2, lang='dutch', num=10, stop=10,)
Res_WP = []
count = 0
for url in results_WP:
    #print(url)
    if url not in Res_Alg:
        Res_WP.append(url)
        if count < 2: Res_Alg.append(url)
        count +=1

zoekterm3 = exactname +' AND '+ werkgever
results_WG = search(zoekterm3, lang='dutch', num=10, stop=10,)
Res_WG = []
count = 0
for url in results_WG:
    #print(url)
    if url not in Res_Alg:
        Res_WG.append(url)
        if (count < 3) and (not 'crdev' in url) : Res_Alg.append(url)
        count += 1

print(f'Belangrijkste websites voor {zoekterm}: \n')
for url in Res_Alg:
    print(url)

print(Res_Alg)
