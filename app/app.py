from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/areas')
def areas():
    return render_template('areas.html')

@app.route('/catalogos')
def catalogos():
    return render_template('catalogos.html')

@app.route('/explorar')
def explorar():
    return render_template('explorar.html')

@app.route('/busqueda')
def busqueda():
    return render_template('busqueda.html')

@app.route('/creditos')
def creditos():
    return render_template('creditos.html')


