from flask import render_template,request,redirect,session,flash
from flask_app.models import recipes #enter model name`
from flask_app import app


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    all_recipes = recipes.Recipe.get_all()
    return render_template("dashboard.html",all_recipes=all_recipes)

@app.route('/recipes/<int:id>')
def recipe(id):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    one_recipe = recipes.Recipe.get_one(id=id)
    return render_template('recipe.html',one_recipe=one_recipe)

@app.route('/create/recipe')
def create_recipe():
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    one_recipe = recipes.Recipe.get_one(id=id)
    return render_template('edit.html', one_recipe=one_recipe)

@app.route('/destroy/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    recipes.Recipe.destroy(id=id)
    return redirect('/dashboard')


@app.post('/create/recipe/new')
def create_new_recipe():
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    if not recipes.Recipe.recipe_validate(request.form):
        return redirect('/create/recipe')
    recipes.Recipe.add_recipe(request.form)
    return redirect('/dashboard')

@app.post('/edit/recipe/<int:id>')
def update_recipe(id):
    data = {
        **request.form,
        "id":id
    }
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/')
    if not recipes.Recipe.recipe_validate(request.form):
        return redirect(f'/edit/{id}')
    recipes.Recipe.update_recipe(data)
    return redirect(f'/recipes/{id}')

