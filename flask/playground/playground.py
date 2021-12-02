from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<play>')
def play(play,num= 3,color="lightblue"):
    return render_template("index.html",  play=play,num=num,color=color )
    

@app.route('/<play>/<int:num>')
def num_box(play, num,color="lightblue"):
    return render_template("index.html",  play=play , num=num, color=color )
    
@app.route('/<play>/<int:num>/<color>')
def color(play,num,color):
    return render_template("index.html",  play=play , num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)