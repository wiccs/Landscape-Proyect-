from flask import Flask

app = Flask(__name__)

from app import routes  # Importamos las rutas desde el archivo routes.py
