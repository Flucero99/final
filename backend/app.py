# ------------------------------------------------------ Archivos

from pagina import app, port
from pagina.models import db

# ------------------------------------------------------------------------------------------ Main

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=port)