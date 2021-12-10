from flask import render_template,request,redirect,session
from flask_app.models import dojos
from flask_app import app





@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result/<string:name>')
def result(name):
    data = {
        "name":name
    }
    one_dojo = dojos.Dojo.get_one(data)
    return render_template('result.html',one_dojo=one_dojo )

@app.post('/process')
def process():
    data = {
        **request.form
    }
    if not dojos.Dojo.validate_dojo(data):
        return redirect('/')
    print(data)
    dojos.Dojo.add_dojo(data)
    return redirect(f'/result/{data["name"]}')



# @app.post('/process')
# def form_info():
#     questions["Your name"] = request.form['Your name']
#     questions['Location'] = request.form['Location']
#     questions['Favorite Language'] = request.form['Favorite Language']
#     questions['Comment'] = request.form['Comment']
#     session['q']= questions

#     return redirect('/result')
    