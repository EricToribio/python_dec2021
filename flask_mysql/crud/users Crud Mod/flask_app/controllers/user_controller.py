from flask import render_template,request,redirect,session,url_for
from flask_app.models import user
from flask_app import app


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/read')
def read_all():
    users = user.User.get_all()
    print(users)
    return render_template("read_all.html",users = users)
    

@app.route('/users/<int:num>')
def show_1(num):
    data ={
        "id": num
    }
    some_user = user.User.get_one(data)
    
    return render_template('read_one.html', some_user=some_user)

@app.route('/users/<int:num>/edit')
def edit_user(num):
    data ={
        "id": num
    }
    some_user = user.User.get_one(data)
    return render_template('edit_user.html', some_user=some_user)

@app.post('/add_user')
def enter():
    
    user.User.add_user(request.form)
    return redirect('/read')

@app.post('/update/<int:num>')
def edit(num):
    user_data ={
        **request.form,
        "id":num
    }
    user.User.edit(user_data)
    print(request.form)
    
    return redirect(f"/users/{num}")

@app.route('/users/<int:num>/destroy')
def delete(num):
    data = {
        "id":num
    }
    user.User.destroy(data)
    return redirect("/read")




@app.route('/create')
def create_user():
    return render_template("createNew.html")
