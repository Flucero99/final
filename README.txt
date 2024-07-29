Activar env:         -> source env/bin/activate <- 
                     ->        deactivate       <- Salir

Iniciar servidor:    -> python3 ./backend/app.py <-
                     ->        Ctrl + C          <- Salir

Psql - Usuario :     -> sudo -i -u postgres <- 
                     ->  ctrl + d or exit   <- Salir
Psql:
       Commandos:
                     \du                  - Listar usuarios y roles
                     \l                   - Listar DB
                     \c <db-nombre>       - Conectar a una DB
                     \dt                  - Listar tablas de la DB
                     \d <tabla-nombre>    - Describir tabla
                     \i                   - Ejecutar comandos de un archivo
                     \q                   - Salir

        Servicio:
                    sudo systemctl status postgresql.service    - Estado del servicio
                    sudo systemctl start postgresql.service     - Iniciar servicio
                    sudo systemctl stop postgresql.service      - Parar servicio
                    sudo systemctl restart postgresql.service   - Reiniciar servicio

Extras:
        Si apretaste Ctrl + Z en la terminal:
                                                fg              - Incia el proceso en el foreground
                                                bg              - Incia el proceso en el background

Dependencias:
    Flask 
    Flask-sqlalchemy
    Flask-wtf
    psycopg2-binary