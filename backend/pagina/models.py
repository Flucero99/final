from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(length=15), nullable=False, unique=True)
    # contra_hash = db.Column(db.String(length=60), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())
    tareas = db.relationship('Tarea', backref='propietario', lazy=True)

    # def __init__(self, nombre):
    #     self.nombre = nombre

    # def registrar_usario(self):
    #     db_usuario = Usuario.query.filter(Usuario.nombre == self.nombre).all()
    #     if not db_usuario:
    #         db.session.add(self)
    #         db.session.commit
    #     return True

    # def obtener_usuario(nombre):
    #     db_usuario = Usuario.query.filter(Usuario.nombre == nombre).first()
    #     return db_usuario

    # def obtener_diccionario(self):
    #     return {
    #         "id": self.id,
    #         "nombre": self.nombre,
    #         "fecha_creacion": self.fecha_creacion,
    #     }

    # def __repr__(self):
    #     return f"<User {self.nombre}>"


class Tarea(db.Model):
    __tablename__ = "tareas"
    id = db.Column(db.Integer, primary_key=True)
    id_propietario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    contenido = db.Column(db.String(length=80), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())

    # def __init__(self, id_propietario, contenido):
    #     self.id_propietario = id_propietario
    #     self.contenido = contenido

    # def obtener_diccionario(self):
    #     return {
    #         "id": self.id,
    #         "id_propietario": self.id_propietario,
    #         "contenido": self.contenido,
    #         "fecha_creacion": self.fecha_creacion,
    #     }

    # def __repr__(self):
    #     return f"<Tarea {self.id}, propietario {self.id_propietario}>"
