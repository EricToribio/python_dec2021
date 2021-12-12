from flask import render_template,request,redirect,session,flash
from flask_app.models import users #enter model name`
from flask_app import app,bcrypt



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/logout')
def logout():
    session.clear()
    flash("You have successfully logged out")
    return redirect('/')

@app.post('/create/user')
def create_user():
    print(request.form)
    if not users.User.validate_new_user(request.form):
        return redirect('/')
    user_id = users.User.add_user(request.form)
    flash('Account Created Please Sign In')
    return redirect('/')

@app.post('/login')
def login():
    user = users.User.get_one(email=request.form['email'])
    if not user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user.id
    session['first_name'] = user.first_name

    return redirect('/dashboard')

