from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class BookDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resumo_longo = db.Column(db.Text)
    isbn = db.Column(db.String(50))
    
    def __init__(self, resumo_longo, isbn):
        self.resumo_longo = resumo_longo
        self.isbn = isbn

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    autor = db.Column(db.String(150))
    ano_publicacao = db.Column(db.Integer)
    assunto = db.Column(db.String(150))
    
    book_detail_id = db.Column(db.Integer, db.ForeignKey('book_detail.id'))
    detail = db.relationship('BookDetail', backref=db.backref('book', uselist=False))
    
    def __init__(self, titulo, autor, ano_publicacao, assunto, book_detail_id=None):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.assunto = assunto
        self.book_detail_id = book_detail_id