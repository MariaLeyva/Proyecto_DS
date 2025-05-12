import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_JSON = os.path.join(BASE_DIR, 'datos', 'json', 'revistas.json')
    OUTPUT_JSON = os.path.join(BASE_DIR, 'datos', 'json', 'revistas_scimagojr.json')
    BACKUP_JSON = os.path.join(BASE_DIR, 'datos', 'json', 'revistas_scimagojr_backup.json')
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
