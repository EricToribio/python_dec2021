from flask import Flask, render_template,request,redirect,session
import user
DB = "users_schema"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/read')
def read():
    users = user.User.get_all()
    print(users)
    return render_template("read_all.html",users = users)
    

@app.post('/enter')
def enter():
    
    user.User.add_user(request.form)
    return redirect('/read')


if __name__ == "__main__":
    app.run(debug=True)