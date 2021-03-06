from flask import Flask, render_template,session,redirect,request
import datetime
import random
app = Flask(__name__)
app.secret_key = 'gold'

@app.route('/')
def index():
    
    if "gold" not in session:
        session["gold"] = 0

    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def gold_rush():
    
    if request.form["location"] == "farm":
        print('hello')
        amt_gold = random.randint(10, 21)
        
    elif request.form["location"] == "cave":
        amt_gold = random.randint(5, 11)

    elif request.form["location"] == "house":
        amt_gold = random.randint(2, 6)
        
    elif request.form["location"] == "casino":
        amt_gold = random.randint(-50,50)
        
    now = datetime.datetime.now()
    if amt_gold > 0:
        session['log'] = f"<p class=text_log> Congratulations! You've won {amt_gold} gold!! {now}</p>"
    else:
        session['log'] = f"<p class=text_log> Oh no! You've lost {amt_gold} gold!! {now}</p>"
    # session["activity_log"].append(log)
    session["gold"] += amt_gold
    return redirect("/")


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
