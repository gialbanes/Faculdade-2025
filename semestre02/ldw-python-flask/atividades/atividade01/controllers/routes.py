from flask import Flask, render_template, request, redirect, url_for

def init_app(app):
    ingredients = ['Giovana', 'Amanda', 'Igor', 'Diego']
    recipeList = [{'Título': 'CS 1.6', 'Ano': 1996, 'Categoria': 'FPS Online'}]
    
    @app.route('/')
    def home():
        return render_template('base.html')
    
    
    @app.route('/recipes', methods=['GET', 'POST'])
    def recipes():
        if request.method == 'POST':
            if request.form.get('recipe'):
                ingredients.append(request.form.get('recipe'))
                return redirect(url_for('recipes'))
                
        return render_template('recipes.html', ingredients=ingredients)
    
    @app.route('/newRecipe', methods=['GET', 'POST'])
    def newRecipe():
        if request.method == 'POST':
            if request.form.get('name') and request.form.get('ingredients') and request.form.get('nacionality'):
                recipeList.append({'Nome': request.form.get('name'), 'Ingredientes': request.form.get('ingredients'), 'Nacionalidade' : request.form.get('nacionality')})
                return redirect(url_for('newRecipe'))
                
        return render_template('newRecipe.html', recipeList=recipeList)