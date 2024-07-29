from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2
# import os
# SECRET_KEY = os.urandom(32)


app = Flask(
    __name__,
    template_folder="../../frontend/templates",
    static_folder="../../frontend/assets",
)
port = 5000
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://postgres:123@localhost:5432/python_flask"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '1234'
# conn = psycopg2.connect(database="python_flask", user="postgres", password="123", host="localhost", port=port)

# ------------------------------------------------------ Archivos

from pagina import rutas

# ------------------------------------------------------ 