"""
==========================================================================================
=       =============================================================  ===================
=  ====  ============================================================  ===================
=  ====  ============================================================  ===================
=  ====  ==  ===   ====   ====   =========   ====   ===  = ====   ===  ======   ===      =
=  ====  ======  =  ==  =  ==     =======  =  ==  =  ==     ==  =  ==    ===  =  ======  =
=  ====  ==  ==     ===    ==  =  ========  =======  ==  =  ==  =====  =  ==     =====  ==
=  ====  ==  ==  ========  ==  =  =========  ====    ==  =  ==  =====  =  ==  =======  ===
=  ====  ==  ==  =  ==  =  ==  =  =======  =  ==  =  ==  =  ==  =  ==  =  ==  =  ===  ====
=       ===  ===   ====   ====   =========   ====    ==  =  ===   ===  =  ===   ===      =
==========================================================================================

"""


import requests
import time
from bs4 import BeautifulSoup
import json
import os.path



data = {}
data['Productos'] = []


lista_categoria = ['tablets', 'televisores-video', 'notebooks', 'living','box-americanos','refrigeradores','comedores']

for index in lista_categoria:

    url = 'https://www.abcdin.cl/tienda/es/abcdin/celulares/'+index
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    cantidad = soup.find('div', class_='pageControl number')


    try:
        can = int(cantidad.find_all('a')[2].get_text().strip())
        print(can)

    except IndexError:
        can = int(cantidad.find_all('a')[1].get_text().strip())
        print(can)

    index_produtos = 0
    for a in range(1, can+1):
        url = 'https://www.abcdin.cl/tienda/es/abcdin/celulares/'+index+'#facet:&productBeginIndex:' + str(
            index_produtos) + '&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&'
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")



        for b in range(1, 25):
            div = soup.find_all('div', class_='product')[b]
            name = div.find('div', class_='product_name').get_text()
            price_i = div.find('span', class_='internetPrice').get_text()
            price_n = div.find('span', class_='normalPrice').get_text()
            url = div.find('div', class_='image')
            url_producto = url.find('a')

            data['Productos'].append({
                'pagina': soup.title.string,
                'nombre': name.strip(),
                'precio-internet': price_i.strip(),
                'precio-normal': price_n.strip(),
                'fecha': time.strftime("%d/%m/%y"),
                'url_producto': url_producto.get('href').strip()})
            pass
        time.sleep(5)
        print('pasaron 5 seg')
        index_produtos = index_produtos + 24
        pass

    dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

    file_name = index+"data-" + time.strftime("%m-%d-%Y-%H-%M-%S") + '.json'

    with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    data = {}
    data['Productos'] = []
    pass













