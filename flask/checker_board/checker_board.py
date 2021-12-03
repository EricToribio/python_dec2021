from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
@app.route('/<int:num1>')
@app.route('/<int:num1>/<int:num2>')
@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def num2(num1=8,num2=8,color1="red",color2="black"):
    return render_template("index.html", num1=num1,num2=num2,color1=color1,color2=color2)




if __name__ == "__main__":
    app.run(debug=True)