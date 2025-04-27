import requests
from bs4 import BeautifulSoup
import json
import time

# Función para obtener la información de una revista
def obtener_informacion_revista(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        # Realizar solicitud HTTP
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        
        # Parsear el contenido de la página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer la información relevante de la página de la revista
        info = {}
        
        # Ejemplo de cómo obtener el H-Index
        h_index = soup.find('span', class_='hindex')  # La clase 'hindex' puede variar
        if h_index:
            info['h_index'] = h_index.text.strip()
        else:
            info['h_index'] = 'No disponible'
        
        # Obtener otras información relevante (aquí deberías ajustar según la estructura HTML)
        info['publisher'] = soup.find('div', class_='publisher').text.strip() if soup.find('div', class_='publisher') else 'No disponible'
        info['issn'] = soup.find('span', class_='issn').text.strip() if soup.find('span', class_='issn') else 'No disponible'
        info['subject_area'] = soup.find('div', class_='subject_area').text.strip() if soup.find('div', class_='subject_area') else 'No disponible'
        info['publication_type'] = soup.find('div', class_='publication_type').text.strip() if soup.find('div', class_='publication_type') else 'No disponible'
        info['widget'] = soup.find('div', class_='widget').text.strip() if soup.find('div', class_='widget') else 'No disponible'
        info['website'] = url
        
        return info

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la página de la revista {url}: {e}")
        return None


# Función para realizar el scraping en el catálogo de revistas
def scraper_catalogo():
    # URL de la página de SCImago (deberías tener las URLs de las revistas que deseas analizar)
    url_catalogo = 'https://www.scimagojr.com/journalrank.php'
    
    # Realizar la solicitud a SCImago
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        # Obtener la página del catálogo general
        response = requests.get(url_catalogo, headers=headers)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        
        # Parsear el contenido de la página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar la tabla de revistas (esto puede cambiar dependiendo del HTML)
        table = soup.find('table', {'class': 'table table-striped'})
        
        # Crear un diccionario para almacenar las revistas
        revistas = {}
        
        # Iterar sobre las filas de la tabla (ignoramos la fila de cabecera)
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) > 1:  # Verificar que la fila tiene columnas
                title = cols[1].text.strip()  # Título de la revista en la segunda columna
                journal_url = cols[1].find('a')['href']  # URL de la revista en el enlace
                
                # Verificar si ya hemos extraído los datos de esta revista
                if title not in revistas:
                    print(f"Obteniendo datos de la revista: {title}")
                    revista_info = obtener_informacion_revista(journal_url)
                    
                    if revista_info:
                        revistas[title] = revista_info
                    time.sleep(2)  # Pausa para evitar hacer demasiadas solicitudes seguidas
        
        # Guardar los datos extraídos en un archivo JSON
        with open('revistas_scimago.json', 'w', encoding='utf-8') as json_file:
            json.dump(revistas, json_file, ensure_ascii=False, indent=4)
        
        print("Scraping completado y datos guardados en 'revistas_scimago.json'.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el catálogo de revistas: {e}")


# Ejecutar el scrapper
if __name__ == '__main__':
    scraper_catalogo()
