from flask import Flask, render_template, request, redirect,session
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret,keep it safe'
@app.route("/")
def store():
    return render_template("dojo_fruit.html")

@app.route("/checkout", methods=["POST"])
def summary():
    session['name']=request.form["name"]
    session['student_id']=request.form["student_id"]
    session['strawberries']=request.form["strawberries"]
    session['raspberries']=request.form["raspberries"]
    session['apples']=request.form["apples"]
    session['oranges']=request.form["oranges"]
    session['bananas']=request.form["bananas"]
    session['count']= int (session['strawberries'])+int(session['raspberries'])+int(session['apples'])+int(session['oranges'])+int(session['bananas'])
    now=datetime.datetime.now()
    session['timestamp']=now.strftime("%B %d %Y %I:%M %p")
    return redirect("/show")
@app.route("/show")
def show_result():
    return render_template("checkout.html")
if __name__=="__main__":
    
    app.run(debug=True) 