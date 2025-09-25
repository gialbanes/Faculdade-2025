from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    autor = db.Column(db.String(150))
    ano_publicacao = db.Column(db.Integer)
    assunto = db.Column(db.String(150))
    
    def __init__(self, titulo, autor, ano_publicacao, assunto):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.assunto = assunto
        
