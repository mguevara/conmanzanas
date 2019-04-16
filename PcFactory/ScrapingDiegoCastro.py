#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
import json
import os

data = {}
data['Productos'] = []
data2 = {}
data2['Productos'] = []

ssl._create_default_https_context = ssl._create_unverified_context

my_url = 'https://www.pcfactory.cl/notebooks?categoria=735&papa=636'
my_url2 = 'https://www.pcfactory.cl/juegos?categoria=657&papa=374'
uClient = uReq(my_url)
uClient2 = uReq(my_url2)
page_html = uClient.read()
page_html2 = uClient2.read()
uClient.close()
uClient2.close()

page_soup = soup(page_html, 'html.parser')
page_soup2 = soup(page_html2, 'html.parser')

containers = page_soup.find_all("div", {"class": "wrap-caluga-matrix"})
containers2 = page_soup2.find_all("div", {"class": "wrap-caluga-matrix"})
contain = containers[0]
contain2 = containers2[0]

#Notebooks

for contain in containers:
    links = contain.find_all("div", {"class": "center-caluga"})[0].find_all("a",{"class": "noselect"})[0]
    titulo = links.find_all("span", {"class": "nombre"})[0].text
    precio = links.find_all("div", {"class" : "caluga-txt"})[0].find_all("span", {"class" : "txt-precio"})[0].text.replace(" ", "")
    marca  = links.find_all("span", {"class": "marca"})[0].text
    print("Producto: " + titulo + " | precio: " + precio + " | marca: " + marca)
     
    data['Productos'].append({
        'Nombre': titulo,
        'Precio': precio,  
        'Marca' : marca,
        })  
    
dire = os.path.dirname(os.path.abspath('__file__')) + '/data'

with open(os.path.join(dire, 'Notebooks.json'), 'w',encoding="utf-8") as file:
     json.dump(data, file, indent=3, ensure_ascii=False)
    
#Juegos    
    
for contain2 in containers2:
    links2 = contain2.find_all("div", {"class": "center-caluga"})[0].find_all("a",{"class": "noselect"})[0]
    titulo2 = links2.find_all("span", {"class": "nombre"})[0].text
    precio2 = links2.find_all("div", {"class" : "caluga-txt"})[0].find_all("span", {"class" : "txt-precio"})[0].text.replace(" ", "")
    marca2 = links2.find_all("span", {"class": "marca"})[0].text
    print("Producto: " + titulo2 + " | precio: " + precio2 + " | marca: " + marca2)
    
    data2['Productos'].append({
        'Nombre': titulo2,
        'Precio': precio2,  
        'Marca' : marca2,
        }) 
    
with open(os.path.join(dire, 'Juegos.json'), 'w',encoding="utf-8") as file:
     json.dump(data2, file, indent=3, ensure_ascii=False)    


# In[ ]:




