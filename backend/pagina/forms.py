from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from pagina.models import Usuario, Tarea

class FormRegistro(FlaskForm):
    nombre = StringField(label="Usuario", validators=[Length(min=4,max=15), DataRequired()])
    submit = SubmitField(label="Enviar")

    def validate_nombre(self, nombre_pendiente):
        usuario = Usuario.query.filter_by(nombre=nombre_pendiente.data).first()
        if usuario:
            raise ValidationError('Ya existe ese usuario! - Intente otro nombre')

class FormTarea(FlaskForm):
    tarea = StringField(label="Tarea: ", validators=[Length(min=5,max=80), DataRequired()])
    submit = SubmitField(label="Agregar tarea")
