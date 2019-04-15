from bs4 import BeautifulSoup
import requests
import json
import os.path


datos={}
datos['productos']=[]

url="https://hmotores.cl/repuestos/"

mostrar=requests.get(url)
contenido=BeautifulSoup(mostrar.content)

for x in range(0,6):
    descripcion =contenido.find_all('div',class_='mov-3 model model-repuesto')[x]
    descripciontext= descripcion.find('h2')
    
    precio_an=contenido.find_all('span',class_='price old')[x]  
    precio=contenido.find_all('span',class_='price')[x] 

    datos['productos'].append({
             'nombre': descripciontext.text,
             'precio_antiguo':precio_an.text,
             'precio_actual':precio.text,
    })
dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

file_name ='archivo.json'

with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
         












