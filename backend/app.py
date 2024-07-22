from flask import Flask, render_template, request,  url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/assets")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     contenido = db.Column(db.String(40), nullable=False)
#     fecha_creacion = db.Column(db.DateTime, default = datetime.now)

#     def __repr__ (self):
#         return '<Tarea %r>' % self.id

@app.route("/", methods = ['POST','GET'])
def hello_world():
    if request.method == 'POST':
        pass
    else:
        return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)