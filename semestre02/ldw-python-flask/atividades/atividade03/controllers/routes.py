import urllib.request
import json
from flask import Flask, render_template, request, redirect, url_for

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

