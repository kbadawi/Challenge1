import urllib.request
import re
import string
import html.parser

#J'initialise mon fichier data
f = open('data.csv', 'w', encoding='UTF-8')
f.write('Nom;Prix\n')
f.closed

#j'isole tout les articles dans une liste
htmllink = urllib.request.urlopen("http://www.ebay.fr/sch/i.html?_nkw=chaise&ssPageName=GSTL")
regexname = b'<h3 class="lvtitle">(.+?)</li>'
regexname = re.compile(regexname, re.DOTALL)
with htmllink as url:
    htmlcode = url.read()
    articles = re.findall(regexname,htmlcode)

#Pour chaque article je préléve les données et gère les cas particuliers
for article in articles:
    article = article.decode("UTF-8")
    article = article.replace(';',' ')
    article = article.replace('<span class="newly">Nouvelle annonce</span>','')
    article = article.replace('\n\t\t\t\t\t','')
    article = article.encode("UTF-8")
    name = re.findall(b'afficher (.*)">',article)
    price = re.findall(b'class="bold">(.*) <b>', article)
    price[0] = price[0].decode("UTF-8")
    name[0] = name[0].decode("UTF-8")
#En cas de tranche de prix je modifie la chaine
    price[0] = price[0].replace('<span class="prRange">','')
    price[0] = price[0].replace(' <b>EUR</b> <span>','€ ')
    price[0] = price[0].replace('</span>','')
    html_parser = html.parser.HTMLParser()
    name[0] = html_parser.unescape(name[0])
#Je remplis mon fichier data des données nom et prix
    f = open('data.csv', 'a', encoding='UTF-8')
    f.write(name[0])
    f.write(';')
    f.write(price[0])
    f.write('€\n')
    f.closed


