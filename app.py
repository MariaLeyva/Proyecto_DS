from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import json
import os
from pathlib import Path
from flask_session import Session

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Configuración de la clave secreta para sesiones
app.secret_key = 'clave_secreta_segura'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Cargar datos de revistas
BASE_DIR = Path(__file__).parent
SCIMAGOJR_JSON = BASE_DIR / 'datos' / 'json' / 'revistas_scimagojr.json'
# Ruta del archivo catalogo_general.json
CATALOGO_GENERAL_JSON = BASE_DIR / 'datos' / 'json' / 'catalogo_general.json'

def cargar_datos():
    try:
        with open(CATALOGO_GENERAL_JSON, 'r', encoding='utf-8') as f:
            catalogo_general = json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo {CATALOGO_GENERAL_JSON} no existe.")
        catalogo_general = {}
    except json.JSONDecodeError:
        print(f"Error: El archivo {CATALOGO_GENERAL_JSON} no contiene un JSON válido.")
        catalogo_general = {}

    return catalogo_general, {}, catalogo_general

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/areas')
def areas():
    catalogo_general, _, _ = cargar_datos()
    # Obtener todas las áreas únicas
    areas = set()
    for info in catalogo_general.values():
        areas.update(info.get('areas', []))
    return render_template('areas.html', areas=sorted(areas), revistas=catalogo_general)

# Ruta para la página de catálogos
@app.route('/catalogos')
def catalogos():
    catalogo_general, _, _ = cargar_datos()
    # Obtener lista única de catálogos
    catalogos = set()
    for revista in catalogo_general.values():
        catalogos.update(revista.get('catalogos', []))
    return render_template('catalogos.html', catalogos=sorted(catalogos))

# Ruta para la página de explorar
@app.route('/explorar')
def explorar():
    return render_template('explorar.html')

# Eliminada la duplicación de la función buscar
# def buscar():
#     return render_template('buscar.html')

# Ruta para la página de búsqueda
@app.route('/buscar')
def buscar():
    query = request.args.get('q', '').lower()
    if not query:
        print("Debug: No query provided.")
        return render_template('buscar.html', revistas={})

    catalogo_general, _, _ = cargar_datos()
    print(f"Debug: Query received: {query}")
    print(f"Debug: Total revistas loaded: {len(catalogo_general)}")

    # Buscar revistas que contengan la consulta
    resultados = {
        titulo: info for titulo, info in catalogo_general.items()
        if query in titulo.lower()
    }
    print(f"Debug: Filtered results: {len(resultados)}")

    return render_template('buscar.html', revistas=resultados, scimagojr={}, query=query)

# Ruta para la página de créditos
@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

@app.route('/area/<area>')
def area_detalle(area):
    catalogo_general, _, _ = cargar_datos()
    # Filtrar revistas por área
    revistas_area = {
        titulo: info for titulo, info in catalogo_general.items()
        if area in info.get('areas', [])
    }
    return render_template('area_detalle.html', area=area, revistas=revistas_area, scimagojr={})

@app.route('/catalogo/<catalogo>')
def catalogo_detalle(catalogo):
    catalogo_general, _, _ = cargar_datos()
    # Filtrar revistas por catálogo
    revistas_catalogo = {
        titulo: info for titulo, info in catalogo_general.items()
        if catalogo in info.get('catalogos', [])
    }
    return render_template('catalogo_detalle.html', catalogo=catalogo, revistas=revistas_catalogo, scimagojr={})

@app.route('/explorar/<letra>')
def explorar_letra(letra):
    catalogo_general, _, _ = cargar_datos()
    print(f"Debug: Letra recibida: {letra}")
    print(f"Debug: Total revistas cargadas: {len(catalogo_general)}")

    # Filtrar revistas por letra inicial
    revistas_letra = {
        titulo: info for titulo, info in catalogo_general.items()
        if titulo.lower().startswith(letra.lower())
    }
    print(f"Debug: Revistas filtradas por letra '{letra}': {len(revistas_letra)}")

    return render_template('explorar_letra.html', letra=letra, revistas=revistas_letra, scimagojr={})

@app.route('/revista/<titulo>')
def revista_detalle(titulo):
    catalogo_general, _, _ = cargar_datos()
    revista_info = catalogo_general.get(titulo, {})
    scimagojr_info = {}
    return render_template('revista_detalle.html', 
                         titulo=titulo, 
                         revista=revista_info, 
                         scimagojr=scimagojr_info)

# Ruta para iniciar sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validar credenciales (esto es un ejemplo simple)
        if email == 'usuario@ejemplo.com' and password == 'contraseña':
            session['user'] = {
                'name': 'Juan Pérez',
                'email': email
            }
            return redirect(url_for('index'))  # Redirigir a la página de inicio
        else:
            return render_template('inicio_sesion.html', error='Credenciales incorrectas')

    return render_template('inicio_sesion.html')

# Ruta para el perfil
@app.route('/perfil')
def perfil():
    if 'user' not in session:
        return redirect(url_for('login'))

    user = session['user']
    return render_template('perfil.html', user=user['name'])

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/add_to_profile', methods=['POST'])
def add_to_profile():
    if 'user' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado."}), 401

    data = request.get_json()
    title = data.get('title')

    if not title:
        return jsonify({"success": False, "message": "Título no proporcionado."}), 400

    # Simular agregar el artículo al perfil del usuario
    user = session['user']
    if 'saved_articles' not in user:
        user['saved_articles'] = []

    user['saved_articles'].append(title)
    session['user'] = user

    return jsonify({"success": True, "message": "Artículo agregado al perfil."})

@app.route('/newnoticias')
def newnoticias():
    return render_template('Newnoticias.html')

@app.route('/catalogo_general')
def catalogo_general():
    _, _, catalogo_general = cargar_datos()
    print(f"Debug: Datos cargados para catalogo_general: {catalogo_general}")
    return render_template('catalogo_general.html', catalogo_general=catalogo_general)

if __name__ == '__main__':
    app.run(debug=True)
