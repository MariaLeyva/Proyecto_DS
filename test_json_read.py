import json
from pathlib import Path

# Define paths
BASE_DIR = Path(__file__).parent
CATALOGO_GENERAL_JSON = BASE_DIR / 'datos' / 'json' / 'catalogo_general.json'
REVISTAS_JSON = BASE_DIR / 'datos' / 'json' / 'revistas.json'

print("Starting JSON read test...")
print(f"Path to catalogo_general.json: {CATALOGO_GENERAL_JSON}")
print(f"Path to revistas.json: {REVISTAS_JSON}")

# Test reading catalogo_general.json
try:
    with open(CATALOGO_GENERAL_JSON, 'r', encoding='utf-8') as f:
        catalogo_general = json.load(f)
    print("catalogo_general.json loaded successfully.")
    print(f"Number of entries: {len(catalogo_general)}")
except Exception as e:
    print(f"Error reading catalogo_general.json: {e}")

# Test reading revistas.json
try:
    with open(REVISTAS_JSON, 'r', encoding='utf-8') as f:
        revistas = json.load(f)
    print("revistas.json loaded successfully.")
    print(f"Number of entries: {len(revistas)}")
except Exception as e:
    print(f"Error reading revistas.json: {e}")
