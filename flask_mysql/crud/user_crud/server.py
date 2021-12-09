from flask import Flask, render_template,request,redirect,session,url_for
import user
DB = "users_schema"
app = Flask(__name__)

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

@app.post('/update')
def edit():
    user.User.edit(request.form)
    print(request.form)
    
    return redirect(f"users/{request.form['id']}")

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

if __name__ == "__main__":
    app.run(debug=True)