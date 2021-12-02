from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",num1=int(8),num2=8)

@app.route('/<int:num1>')
def num1(num1):
    return render_template("index.html",num1=num1,num2=8)

@app.route('/<int:num1>/<int:num2>')
def num2(num1,num2):
    return render_template("index.html", num1=num1,num2=num2)


if __name__ == "__main__":
    app.run(debug=True)