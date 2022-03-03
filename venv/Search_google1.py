import requests
import json
import urllib
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os, time
from datetime import datetime

dateTimeObj = datetime.now()

def Woorden(text_soup):
    Hoofdletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyzïàë'
    tekens = ['/[]{}\|_']
    woorden = []
    for woord in text_soup:
        Teken_letter = True
        for letter in Woord:
            if letter in tekens: Teken_letter = False
            if (letter in letters) and Teken_letter:
                Teken_letter = True
            else:
                Teken_letter = False
        try:
            if (Woord[0] in Hoofdletters) and (len(Woord) > 4) and Teken_letter:
                woorden.append(Woord)
        except:
            pass
    return woorden


def Text_termen_url(url):
    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        for script in soup(["script", "style"]):
           script.extract()  # rip it out

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text
    except:
        return 'niets'

zoekterm = 'Kobus Bijker'
woonplaats = 'Winsum'
werkgever = 'Hanzehogeschool'




#zoekterm = input('Naam persoon: ')
#woonplaats = input('Woonplaats (?=niet weten of op zoeken): ')
#werkgever = input('Werkgever/School (?=niet weten of op zoeken): ')

exactname = '['+zoekterm+']'
results_EN = search(zoekterm, lang='english', num=10, stop=10,)
Res_Alg = []
print(f'OSINT scan via Google advanced Search wordt uitgevoerd voor {zoekterm}...')
for url in results_EN:
    if not 'crdev' in url: Res_Alg.append(url) #cookie websites negeren
    #print(url)

results_NL = search(exactname, lang='dutch', num=10, stop=10,)
Res_NL = []
for url in results_NL:
    if url not in Res_Alg:
        Res_NL.append(url)
        if not 'crdev' in url: Res_Alg.append(url) #cookie websites negeren
        #print(url)
print('Nog even geduld aub...websites worden gescand..')
zoekterm2 = exactname +' AND '+ woonplaats
results_WP = search(zoekterm2, lang='dutch', num=10, stop=10,)
Res_WP = []
count = 0

for url in results_WP:

    if url not in Res_Alg:
        Res_WP.append(url)
        if count < 2: Res_Alg.append(url)
        count +=1

zoekterm3 = exactname +' AND '+ werkgever
results_WG = search(zoekterm3, lang='dutch', num=10, stop=10,)
Res_WG = []
count = 0
print('Nog even geduld aub.....')
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

# Verdere analyse sites;

namen = zoekterm.split(' ')
namen.append(woonplaats)
namen.append(werkgever)
Hoofdletters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyzïàë'
tekens = ['/[]{}\|_']

TekstenInteressant = {}
Termen_url = {}

for url in Res_Alg:
    Termen = []
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")

        Woorden_soup = str(soup).split(' ')
        for Woord in Woorden_soup:
                Teken_letter = True
                for letter in Woord:
                    if letter in tekens: Teken_letter = False
                    if (letter in letters) and Teken_letter:
                        Teken_letter = True
                    else: Teken_letter = False
                if (Woord[0] in Hoofdletters) and (len(Woord) > 4) and Teken_letter:
                        Termen.append(Woord)
    except: print(f'Kan html-content van {url} niet lezen.')
    #print(soup.prettify()) # print the parsed data of html
    tekst = Text_termen_url(url)
    print(tekst)
    if tekst != 'niets':
        Termen1 =Woorden(tekst)
        Termen.append(Termen1)



    try:
        print(soup.title.text)
        content = soup.title.text
        Woorden_content = content.split(' ')
        tel = 0
        for word in namen:
            if word in content and tel ==0 :
               TekstenInteressant[url] = content
               tel+=1
        for Woord in Woorden_content:
                for letter in Woord:
                    if letter in Hoofdletters and len(Woord) > 5:
                        Termen.append(Woord)
        Termen_url[url]= (Termen, content)


    except:
        print(f'Website {url} heeft blijkbaar geen text-title.')

print(Termen_url)
print(TekstenInteressant)

#Rapport wegschrijven
file = f'c:/OSINT/rapport_{zoekterm}.txt'
with open(file, 'w') as f:
    f.write(f'OSINT rapport voor {zoekterm}:\n')
    f.write(f'Gevonden websites:\n')

    for url in Res_Alg:
        f.write(f'{url}\n')
    f.write('-------------------------------------------------------\n')
    f.write(f'Diepgaander info over de gevonden sites:\n')
    for url, termen_cont in Termen_url.items():
        f.write(f'site: {url}:\n')
        f.write(f'titel info: {termen_cont[1]}\n')
        f.write(f'Interessante termen: {termen_cont[0]}\n')
        f.write('-------------------------------------------------------\n')
    f.close()
print(f'Rapport {file} is aangemaakt')
