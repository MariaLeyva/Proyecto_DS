# Explorador de Revistas Académicas — Universidad de Sonora

Sistema web desarrollado en **Python + Flask + Bootstrap** para explorar revistas académicas indexadas en catálogos reconocidos, utilizando datos obtenidos desde **SCIMAGO** y **Resurchify**.

---

## Funcionalidades 
### Parte 1: Conversión CSV → JSON 
- Se procesan archivos desde `datos/csv/areas` y `datos/csv/catalogos`.
- Se genera un diccionario con estructura:
  json
{
  "acta geophysica": {
    "areas": ["CIENCIAS_EXA", "ING"],
    "catalogos": ["JCR", "SCOPUS"]
  }
}

Resultado guardado como datos/json/revistas_base.json.

Parte 2: Web Scraping desde SCIMAGO y Resurchify 
El programa toma los títulos desde revistas_base.json.

Por cada revista obtiene:
🌐 Sitio Web
📊 H-Index
🗂️ Área y Categoría
🏢 Editorial
🔢 ISSN
🔗 Widget

Tipo de Publicación

La información se guarda como revistas_completas.json.
 Parte 3: Aplicación Web 
Interfaz con navegación clara y profesional:
🏠 Inicio: Presentación del sitio.
🧠 Área: Lista de áreas → revistas con H-Index.
📚 Catálogo: Lista de catálogos → revistas.
🔎 Explorar: Navegación alfabética de revistas.
📝 Búsqueda: Tabla dinámica con filtro por texto.
👥 Créditos: Integrantes del equipo.

Todos los estilos usan los colores institucionales de la Universidad de Sonora y el logotipo oficial.
✨ Funcionalidades Extra
Función	
🔐 Login con sesión y favoritos por usuario	
🖼️ Logotipo personalizado del sistema	
⏰ Campo ultima_visita con actualización automática	
🖼️ Capturas y portada de presentación final	
🔍 Datos combinados con Resurchify	

⚙️ Requisitos
Python 3.9+
Flask
BeautifulSoup4
Requests
Bootstrap (vía CDN)

Instalación:
pip install -r requirements.txt

🚀 Cómo ejecutar
1.Convertir CSV a JSON
python utils/csv_to_json.py
2.Ejecutar el Scraper
python app/scrapper.py
3.Iniciar la app web
python app/app.py

👨‍💻 Integrantes del equipo
Nombre	
Maria Jose Leyva Garcia
Luis Gerardo Contreras Anaya
Luis Fernando Mercado Perez


 Asistentes Digitales
Este proyecto utilizó asistencia puntual de herramientas como:
🧠 ChatGPT (OpenAI)
🤖 GitHub Copilot

Las herramientas fueron utilizadas bajo supervisión para acelerar el desarrollo y asegurar la calidad del código.
📄 Licencia
Proyecto con fines educativos – Universidad de Sonora.
