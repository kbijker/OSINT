from bs4 import BeautifulSoup
import requests

zoekterm = 'Kobus Bijker'
woonplaats = 'Winsum'
werkgever = 'Hanzehogeschool'
namen = zoekterm.split(' ')
namen.append(woonplaats)
namen.append(werkgever)
print(namen)
Hoofdletters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyzïàë'
Res = ['https://nl.linkedin.com/in/kobus-bijker-0692901a', 'https://hanzehogeschool.academia.edu/KobusBijker', 'https://www.youtube.com/channel/UCtnsoeYCTgk66prZWWqRFmw', 'https://www.arounddeal.com/profile/kobus-bijker/t2uxnxvbye/', 'https://m.facebook.com/Helderseviskotters/posts/1287096424775470?comment_id=1287129091438870&comment_tracking=%7B%22tn%22%3A%22R%22%7D', 'https://m.facebook.com/Helderseviskotters/posts/998002687018180', 'https://www.online-begraafplaatsen.nl/zerken.asp?sortpers=geboren&command=showgraf&bgp=1439&grafid=1103569&char=B', 'https://www.genealogieonline.nl/en/over-de-dag/1942/09/22', 'http://kobusbijker.blogspot.com/2006/08/kennis-maken.html', 'https://www.hanze.nl/eng/education/engineering/school-of-communication-media--it/organisation/employees/smoelenboek', 'https://winsum.nieuws.nl/sport/20160523/c5/', 'https://issuu.com/goodfield/docs/winsum', 'https://www.youtube.com/watch?v=jr4S3P7IzQw', 'https://www.coursehero.com/file/55023070/Tentamen-1pdf/', 'https://www.arounddeal.com/profile/alex-bijker/c3osfzvacm/']
TekstenInteressant = {}
Termen_url = {}

for url in Res:
    Termen = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    try:
        Woorden_soup = str(soup).split(' ')
        for Woord in Woorden_soup:
                Teken_letter = True
                for letter in Woord:

                    if (letter in letters) and Teken_letter:
                        Teken_letter = True
                    else: Teken_letter = False
                if (Woord[0] in Hoofdletters) and (len(Woord) > 6) and Teken_letter:
                        Termen.append(Woord)
    except: print(f'Kan html-content van {url} niet lezen.')
    #print(soup.prettify()) # print the parsed data of html
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
        Termen_url[url]= Termen


    except:
        print(f'Website {url} heeft blijkbaar geen text-title.')

print(Termen_url)
print(TekstenInteressant)
