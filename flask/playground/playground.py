from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def play(num= 3,color="lightblue"):
    return render_template("index.html",  num=num,color=color )
    



if __name__ == "__main__":
    app.run(debug=True)