# Importando o Flask no pacote API
from flask import Flask
# Importando o Flask-Restful
from flask_restful import Api 
# Importando o Pymongo
from flask_pymongo import PyMongo
# Importando o Flask-Marshmallow
from flask_marshmallow import Marshmallow

# Carregando Flask na variável app
app = Flask(__name__)
# Setando o endereço do banco MongoDB
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api-movies'
# Carregando o pacote Api do Flask Restful
api = Api(app)
# Carregando o PyMongo na variável mongo
mongo = PyMongo(app)
# Carregando o Marshmallow na variável "ma"
ma = Marshmallow(app)

# Importando os recursos
from .resources import movie_resources