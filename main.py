import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree

url = "http://www.helmiau.com/stdiis/#kumpulan-logo"

r = requests.get(url)
Nama_Logo = []
Preview_Link = []
Image_Link = []

soup = BeautifulSoup(r.text, 'html5lib')
table = soup.find_all('table')[-1]
# print(table)

rows = table.find_all('tr')[1:]

for i in rows:
    nama = i.find_all('td')[0].text.strip()
    Nama_Logo.append(nama)

    preview = i.find_all('img')[0].get('src')
    Preview_Link.append(preview)

    link = i.find_all('a')[0].get('href')
    Image_Link.append(link)

    print(nama)
    print(preview)
    print(link)

print(Nama_Logo)
print(Preview_Link)
print(Image_Link)
