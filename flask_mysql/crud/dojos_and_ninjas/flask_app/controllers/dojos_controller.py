from flask import render_template,request,redirect,session
from flask_app.models.dojos import Dojo 
from flask_app.models.ninjas import Ninja
from flask_app import app


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dojos')
def dojos():
    
    all_dojos = Dojo.get_all()
    return render_template('all_dojos.html',all_dojos=all_dojos)

@app.route('/dojo/<int:id>')
def one_dojo(id):
    data ={
        "id": id
    }
    one_dojo = Dojo.get_one(data)
    return render_template('one_dojo.html',one_dojo=one_dojo)

@app.route('/add/ninja')
def add_ninja():
    all_dojos = Dojo.get_all()
    return render_template('add_ninja.html',all_dojos=all_dojos)


@app.post('/add/dojo')
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect ('/dojos')

@app.post('/create/ninja')
def create_ninja():
    data = {
        **request.form
    }
    Ninja.add_ninja(data)
    return redirect(f'/dojo/{data["dojo_id"]}')