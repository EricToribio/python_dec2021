from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/count')
def counter():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)