from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key ="bobsaunt"

questions ={
        "Your name": "",
        "Location": "",
        "Favorite Language": "",
        "Comment": ""
        }
@app.route('/')
def index(questions=questions):
    return render_template("index.html",questions=questions)

@app.route('/result')
def result(questions=questions):
    print(session)
    return render_template('result.html', questions=questions)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')



@app.post('/process')
def form_info():
    questions["Your name"] = request.form['Your name']
    questions['Location'] = request.form['Location']
    questions['Favorite Language'] = request.form['Favorite Language']
    questions['Comment'] = request.form['Comment']
    session['q']= questions

    return redirect('/result')
    
if __name__ == "__main__":
    app.run(debug=True)




