from flask import Flask, render_template, request, redirect, url_for

def init_app(app):
    ingredients = ['Strogonoff', 'Strogonoff', 'Strogonoff']
    recipeList = [{}]
    
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
            if request.form.get('name') and request.form.get('time') and request.form.get('difficulty') and request.form.get('category'):
                recipeList.append({'Nome': request.form.get('name'), 'Tempo': request.form.get('time'), 'Dificuldade' : request.form.get('difficulty'), 'Categoria': request.form.get('category')})
                return redirect(url_for('newRecipe'))
                
        return render_template('newRecipe.html', recipeList=recipeList)