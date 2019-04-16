from bs4 import BeautifulSoup
import requests
import json
import os.path
data = {}
data['Productos'] = []

url="https://simple.ripley.cl/mercado-ripley/tecnologia/computadores"
r = requests.get(url)

soup= BeautifulSoup(r.content, "lxml")

nombre= soup.find_all('div',class_='catalog-product-details__name')
for nombres in nombre:
        print(nombres.text)
        pass

precio= soup.find_all('div',class_='catalog-product-details__prices')
for precios in precio:
        print(precios.text)
        pass
descuento= soup.find_all('div',class_='catalog-product-details__discount-tag')
for descuentos in descuento:
        print(descuentos.text)
        pass 
        
        data['Productos'].append({
        'pagina': soup.title.string,
        'nombre': nombres.text,
        'precio': precios.text,
        'descuento': descuentos.text,
        
                                    })   
                  


dir = os.path.dirname(os.path.abspath('__file__')) + '/data'

file_name = "datos.json"
with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

