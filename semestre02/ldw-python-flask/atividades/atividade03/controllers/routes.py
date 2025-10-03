import urllib.request
import json
from flask import Flask, render_template, request, redirect, url_for
from models.database import db, Book, BookDetail 

def init_app(app):
    book_titles = ['The Lord of the Rings', 'Dune', 'Pride and Prejudice']
    book_list = [{'Título': 'The Hobbit', 'Autor': 'J.R.R. Tolkien', 'Ano_Publicação': 1937, 'Assunto': 'Fantasy'},]
    
    
    @app.route('/')
    def home():
        return render_template('base.html')
    
    @app.route('/books', methods=['GET', 'POST'])
    def books():
        if request.method == 'POST':
            book_title_from_form = request.form.get('book_title')
            if book_title_from_form:
                book_titles.append(book_title_from_form)
                return redirect(url_for('books'))
                
        return render_template('books.html', livrosList=book_titles)
    
    @app.route('/cadbooks', methods=['GET', 'POST'])
    def cadbooks():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('autor') and request.form.get('ano_publicacao') and request.form.get('assunto'):
                book_list.append({'Título': request.form.get('titulo'), 'Autor': request.form.get('autor'), 'Ano_Publicação': request.form.get('ano_publicacao'), 'Assunto': request.form.get('assunto')})
                return redirect(url_for('cadbooks'))
        return render_template('cadbooks.html', book_list=book_list)


    @app.route("/books/estoque", methods=['GET', 'POST'])
    @app.route("/books/estoque/delete/<int:id>")
    def booksEstoque(id=None):
        if id:
            book = Book.query.get(id)
            
            db.session.delete(book)
            db.session.commit()
            return redirect(url_for('booksEstoque'))
        
        if request.method == 'POST':
            newbook = Book(
                request.form['titulo'], 
                request.form['autor'], 
                request.form['ano_publicacao'], 
                request.form['assunto'], 
                request.form.get('book_detail_id') 
            )
            db.session.add(newbook)
            db.session.commit()
            return redirect(url_for('booksEstoque'))
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 3
            books_page = Book.query.paginate(page=page, per_page=per_page)
            book_details = BookDetail.query.all() 
            return render_template('booksestoque.html', booksestoque=books_page, book_details=book_details)
    
    @app.route("/books/edit/<int:id>", methods=['GET', 'POST'])
    def bookEdit(id):
        b = Book.query.get(id)
        if request.method == 'POST':
            b.titulo = request.form['titulo']
            b.autor = request.form['autor']
            b.ano_publicacao = request.form['ano_publicacao']
            b.assunto = request.form['assunto']
            b.book_detail_id = request.form['book_detail_id'] 
            db.session.commit()
            return redirect(url_for('booksEstoque'))
        
        book_details = BookDetail.query.all() 
        return render_template('editBook.html', b=b, book_details=book_details) 
    
    @app.route('/book_details/estoque', methods=['GET', 'POST']) 
    @app.route('/book_details/estoque/delete/<int:id>') 
    def bookDetailsEstoque(id=None):
        if id:
            book_detail = BookDetail.query.get(id) 
            db.session.delete(book_detail)
            db.session.commit()
            return redirect(url_for('bookDetailsEstoque')) 
        
        if request.method == 'POST':
            new_book_detail = BookDetail(request.form.get('resumo_longo', ''), request.form.get('isbn', '')) 
            db.session.add(new_book_detail)
            db.session.commit()
            return redirect(url_for('bookDetailsEstoque')) 
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 3
            book_details_page = BookDetail.query.paginate(page=page, per_page=per_page) 
            return render_template('bookdetailsestoque.html', book_details_estoque=book_details_page) 
    
    @app.route('/book_details/edit/<int:id>', methods=['GET', 'POST']) 
    def bookDetailEdit(id):
        book_detail = BookDetail.query.get(id) 
        if request.method == 'POST':
            book_detail.resumo_longo = request.form['resumo_longo']
            book_detail.isbn = request.form['isbn']
            
            db.session.commit()
            return redirect(url_for('bookDetailsEstoque')) 
        return render_template('editBookDetail.html', book_detail=book_detail) 
    
    
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
