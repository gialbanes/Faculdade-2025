from flask import Flask, render_template
from controllers import routes
import pymysql
from models.database import * 

app = Flask(__name__, template_folder="views")

routes.init_app(app)

# Define o nome do BD
DB_NAME = 'books'
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

if __name__ == '__main__':
    # Conecta ao MySQL para criar o BD, se necessário
    connection = pymysql.connect(host='localhost',
                                 user = 'root',
                                 passwd = '',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # Cria o bd se ele não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f'O banco de dados está criado!')
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
    
    # Inicializa a aplicação Flask
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Inicia o aplicativo Flask
    app.run(host='0.0.0.0', port=4000, debug=True)