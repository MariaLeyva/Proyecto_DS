from flask import Blueprint, render_template # type: ignore

main = Blueprint('main', __name__)

@main.route('/')
def inicio():
    return render_template('inicio.html')

@main.route('/area')
def area():
    return render_template('area.html')

@main.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@main.route('/explorar')
def explorar():
    return render_template('explorar.html')

@main.route('/buscar')
def buscar():
    return render_template('buscar.html')

@main.route('/creditos')
def creditos():
    return render_template('creditos.html')
