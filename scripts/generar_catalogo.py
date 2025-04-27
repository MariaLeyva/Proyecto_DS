import csv
import json
import os

def convertir_a_utf8(directorio):
    for carpeta_raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith('.csv'):
                ruta_archivo = os.path.join(carpeta_raiz, archivo)
                print(f'Convirtiendo: {ruta_archivo}')

                # Leer el archivo original (latin-1)
                with open(ruta_archivo, 'r', encoding='latin-1') as f:
                    contenido = f.read()

                # Sobrescribirlo en UTF-8
                with open(ruta_archivo, 'w', encoding='utf-8') as f:
                    f.write(contenido)

    print('¡Todos los archivos fueron convertidos a UTF-8!')

if __name__ == '__main__':
    convertir_a_utf8('datos/csv')

def generar_catalogo():
    catalogo = {}

    # Leer áreas
    path_areas = 'datos/csv/areas'
    for archivo in os.listdir(path_areas):
        if archivo.endswith('.csv'):
            with open(os.path.join(path_areas, archivo), newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    revista = row[0].strip().lower()
                    area = archivo.replace('.csv', '')
                    if revista not in catalogo:
                        catalogo[revista] = {"areas": [], "catalogos": []}
                    catalogo[revista]["areas"].append(area)
                for row in reader:
                    revista = row[0].strip().lower()
                    area = archivo.replace('.csv', '')
                    if revista not in catalogo:
                        catalogo[revista] = {"areas": [], "catalogos": []}
                    catalogo[revista]["areas"].append(area)

    # Leer catálogos
    path_catalogos = 'datos/csv/catalogos'
    for archivo in os.listdir(path_catalogos):
        if archivo.endswith('.csv'):
            with open(os.path.join(path_catalogos, archivo), newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    revista = row[0].strip().lower()
                    catalogo_nombre = archivo.replace('.csv', '')
                    if revista not in catalogo:
                        catalogo[revista] = {"areas": [], "catalogos": []}
                    catalogo[revista]["catalogos"].append(catalogo_nombre)

    # Guardar JSON
    output_path = 'datos/json/catalogo_general.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(os.listdir(path_catalogos))
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(catalogo, f, indent=4, ensure_ascii=False)

    print(f'Catalogo generado en {output_path}')

if __name__ == '__main__':
    generar_catalogo()
