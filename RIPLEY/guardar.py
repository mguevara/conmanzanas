from bs4 import BeautifulSoup
import requests
import json
import os.path
data = {}
data['Productos'] = []

url="https://simple.ripley.cl/mercado-ripley/tecnologia/computadores"
r = requests.get(url)

soup= BeautifulSoup(r.content, "lxml")


for b in range(14,14):
        nombre= soup.find_all('div',class_='catalog-product-details__name')[b]
        precio= soup.find_all('div',class_='catalog-product-details__prices')[b]
        descuento= soup.find_all('div',class_='catalog-product-details__discount-tag')[b]

        data['Productos'].append({
        'pagina': soup.title.string,
        'nombre':  nombre.text,
        'precio': precio.text,
        'descuento': descuento.text,
                                    })   
        pass
print("json Creado!")


dir = os.path.dirname(os.path.abspath('__file__')) + '/data'

