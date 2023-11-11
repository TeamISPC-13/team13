import requests
from bs4 import BeautifulSoup
import pandas as pd

puestos = []
nombres = []
precios = []
imagen_urls = []

urls = [
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA10233?new_bestseller_landing=true#origin=vip",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA1672?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA1652?attribute_id=BRAND&attribute_value_id=7494&new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA418448?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA1692?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA1693?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA1652?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA14407?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA372127?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA1042?new_bestseller_landing=true#origin=pdp",
    "https://www.mercadolibre.com.ar/mas-vendidos/MLA8618?new_bestseller_landing=true#origin=pdp"
]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        producto_mas_vendido = soup.select_one('.ui-recommendations-card__highlight-deal > span')
        nombre_element = soup.select_one('.ui-recommendations-card__content > p > a')
        precio_element = soup.select_one('.ui-recommendations-card__price-block > div > span')
        imagen_element = soup.select_one('#root-app > section > div > section > section > div > div.ui-recommendations-card.ui-recommendations-card--vertical.show-original-price.__item > div.ui-recommendations-card__image-container > img')

        
        puesto = producto_mas_vendido.text.strip() if producto_mas_vendido else "Puesto no encontrado"
        nombre = nombre_element.text.strip() if nombre_element else "Nombre no encontrado"
        precio = precio_element.text.strip() if precio_element else "Precio no encontrado"
        imagen_url = imagen_element['src'] if imagen_element else "URL de imagen no encontrada"

        
        puestos.append(puesto)
        nombres.append(nombre)
        precios.append(precio)
        imagen_urls.append(imagen_url)
    else:
        print(f"No se pudo acceder a la página: {url}")


data = {
    'Puesto': puestos,
    'Nombre': nombres,
    'Precio': precios,
    'URL de Imagen': imagen_urls
}
df = pd.DataFrame(data)


df.to_excel('productos_vendidos.xlsx', index=False)