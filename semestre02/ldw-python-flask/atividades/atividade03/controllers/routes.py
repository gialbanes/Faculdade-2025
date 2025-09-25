import urllib.request
import json
from flask import Flask, render_template, request, redirect, url_for
from models.database import db, Book

def init_app(app):
    # Usaremos listas para simular o banco de dados de livros
    book_titles = ['The Lord of the Rings', 'Dune', 'Pride and Prejudice']
    book_list = []
    
    @app.route('/')
    def home():
        return render_template('base.html')
    
    @app.route('/books', methods=['GET', 'POST'])
    def books():
        if request.method == 'POST':
            # Adiciona um novo título à lista
            book_title_from_form = request.form.get('book_title')
            if book_title_from_form:
                book_titles.append(book_title_from_form)
                return redirect(url_for('books'))
                
        return render_template('books.html', livrosList=book_titles)
    
    @app.route('/newBook', methods=['GET', 'POST'])
    def newBook():
        if request.method == 'POST':
            # Adiciona um novo livro com todos os campos à lista
            book_data = {
                'title': request.form.get('title'),
                'author': request.form.get('author'),
                'publish_year': request.form.get('publish_year'),
                'subject': request.form.get('subject')
            }
            if all(book_data.values()): # Verifica se todos os campos foram preenchidos
                book_list.append(book_data)
                return redirect(url_for('newBook'))
                
        return render_template('newBook.html', bookList=book_list)

    @app.route("/books/estoque", methods=['GET', 'POST'])
    @app.route("/books/estoque/delete/<int:id>")
    def booksEstoque(id=None):
        if id:
            book = Book.query.get(id)
            db.session.delete(book)
            db.session.commit()
            return redirect(url_for('booksEstoque'))
        
        if request.method == 'POST':
            newbook = Book(request.form['titulo'], request.form['autor'], request.form['ano_publicacao'], request.form['assunto'])
            db.session.add(newbook)
            db.session.commit()
            return redirect(url_for('booksEstoque'))
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 3
            books_page = Book.query.paginate(page=page, per_page=per_page)
            return render_template('booksestoque.html', booksestoque=books_page)
    
    @app.route("/books/edit/<int:id>", methods=['GET', 'POST'])
    def bookEdit(id):
        b = Book.query.get(id)
        if request.method == 'POST':
            b.titulo = request.form['titulo']
            b.autor = request.form['autor']
            b.ano_publicacao = request.form['ano_publicacao']
            b.assunto = request.form['assunto']
            db.session.commit()
            return redirect(url_for('booksEstoque'))
    
    @app.route("/apilivros", methods=['GET'])
    @app.route("/apilivros/<string:title>", methods=['GET'])
    def apilivros(title=None):
        if title:
            url_livro = f'https://openlibrary.org/search.json?title={title}'
            try:
                response = urllib.request.urlopen(url_livro)
                data = response.read()
                livros_data = json.loads(data)
                
                if livros_data['docs']:
                    livro_info = livros_data['docs'][0]
                    return render_template('livroInfo.html', livroInfo=livro_info)
                else:
                    return f'Livro com o título "{title}" não encontrado.'
            except Exception as e:
                return f'Erro ao carregar o livro: {e}'
        else:
            url_lista = 'https://openlibrary.org/search.json?q=fiction'
            try:
                response = urllib.request.urlopen(url_lista)
                data = response.read()
                livros_data = json.loads(data)
                livros_list = livros_data.get('docs', [])
                return render_template('apilivros.html', livrosList=livros_list)
            except Exception as e:
                return f'Erro ao carregar a lista de livros: {e}'

