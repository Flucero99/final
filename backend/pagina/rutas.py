from flask import render_template, request, jsonify, url_for, redirect, flash

# ------------------------------------------------------ Archivos

from pagina.models import Usuario, Tarea, db
from pagina import app
from pagina.forms import FormRegistro, FormTarea

# ------------------------------------------------------------------------------------------------------------ Root


@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def root():
    if request.method == "POST":
        pass
    else:
        lista_usuarios = Usuario.query.order_by(Usuario.fecha_creacion).all()
        return render_template("index.html", item_lista=lista_usuarios)


# ------------------------------------------------------------------------------------------------------------ Registro


@app.route("/crear-usuario", methods=["GET", "POST"])
def crear_usuario():
    form = FormRegistro()
    if request.method == "POST":
        if form.validate_on_submit():
            usuario_creado = Usuario(nombre=form.nombre.data)
            db.session.add(usuario_creado)
            db.session.commit()
            return redirect(url_for("root"))
    elif request.method == "DELETE":
        pass
    if form.errors != {}:  # Si hay errores
        for error in form.errors.values():
            flash(f"Hubo un error al crear un usuario: {error}")
    return render_template("crear-usuario.html", item_form=form)


# ------------------------------------------------------------------------------------------------------------ Todo - Pruebas


@app.route("/todo", methods=["GET"])
def todo():
    return render_template("todo.html", item_usuario="Usuario")


# ------------------------------------------------------------------------------------------------------------ Todo - Usuario


@app.route("/todo/<usuario>", methods=["GET", "POST"])
def todo_usuario(usuario):
    usuario_db = Usuario.query.filter_by(nombre=usuario).first()
    form = FormTarea()
    if request.method == "POST":
        if form.validate_on_submit():
            tarea_creada = Tarea(
                id_propietario=usuario_db.id, contenido=form.tarea.data
            )
            db.session.add(tarea_creada)
            db.session.commit()
            return redirect(url_for("todo_usuario", usuario=usuario))
    lista_usuarios = Usuario.query.order_by(Usuario.fecha_creacion).all()
    lista_tareas = Tarea.query.filter_by(id_propietario=usuario_db.id).order_by(Tarea.id).all()
    return render_template(
        "todo.html",
        item_usuario=usuario,
        item_usuarios=lista_usuarios,
        item_tareas=lista_tareas,
        item_form=form,
    )


# ------------------------------------------------------------------------------------------ Eliminar


@app.route("/todo/<usuario>/eliminar/<id>", methods=["POST"])
def eliminar_tarea(usuario, id):
    # usuario_db = Usuario.query.filter_by(nombre=usuario).first()
    tarea_borar = Tarea.query.get_or_404(id)
    try:
        db.session.delete(tarea_borar)
        db.session.commit()
        return redirect(url_for("todo_usuario", usuario=usuario))
    except:
        return "Problema encontrado al borrar"


# ------------------------------------------------------------------------------------------ Editar


@app.route("/todo/<usuario>/editar/<id>", methods=["GET", "POST"])
def editar_tarea(usuario, id):
    # usuario_db = Usuario.query.filter_by(nombre=usuario).first()
    tarea_editar = Tarea.query.filter_by(id=id).first()
    form = FormTarea()
    if request.method == "POST":
        if form.validate_on_submit():
            tarea_editar.contenido = form.tarea.data
            db.session.commit()
            return redirect(url_for("todo_usuario", usuario=usuario))
    else:
        return render_template(
            "/todo-editar.html",
            item_usuario=usuario,
            item_tarea=tarea_editar,
            item_form=form,
        )


# ------------------------------------------------------------------------------------------------------------ Perfil - Pruebas


@app.route("/perfil")
def perfil():
    return render_template("/perfil.html")


# ------------------------------------------------------------------------------------------------------------ Perfil - Usuarios
# ------------------------------------------------------------------------------------------ Editar


@app.route("/perfil/<usuario>", methods=["GET", "POST"])
def perfil_usuario(usuario):
    perfil_editar = Usuario.query.filter_by(nombre=usuario).first()
    form = FormRegistro()
    if request.method == "POST":
        if form.validate_on_submit():
            perfil_editar.nombre = form.nombre.data
            db.session.commit()
            return redirect(url_for("perfil_usuario", usuario=form.nombre.data))
    return render_template(
        "/perfil.html", item_usuario=usuario, item_id=perfil_editar.id, item_form=form
    )


# ------------------------------------------------------------------------------------------ Eliminar


@app.route("/perfil/<usuario>/eliminar/<id>", methods=["POST"])
def eliminar_perfil(usuario, id):
    # usuario_db = Usuario.query.filter_by(nombre=usuario).first()
    perfil_borar = Usuario.query.get_or_404(id)
    try:
        db.session.delete(perfil_borar)
        db.session.commit()
        return redirect(url_for("root"))
    except:
        return "Problema encontrado al borrar perfil"


# ------------------------------------------------------------------------------------------------------------ Pruebas


@app.route("/pruebas")
def pruebas():
    return render_template("/todo-og.html")


@app.route("/pruebas-1")
def pruebas_1():
    return "<body style='background-color: #212121; color: white;'><h1>Que onda gente</h1></body>"
