from flask import Flask, render_template, request, redirect,session, jsonify
import datetime



app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/test')         
def test():
    return "Hello Frm Other Side"


@app.route("/multibly_by_10", methods=['POST'])
def multile_by_10():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json)
        number = json["number"]
        return jsonify(number * 10)
    else:
        return 'Content-Type not supported!'


@app.route('/checkout' , methods=['POST'])         
def checkout():
    form_data = request.form
    session['strawberry'] = form_data["strawberry"]
    session['raspberry'] = form_data['raspberry']
    session['apple'] = form_data['apple']
    session['first_name'] = form_data.get('first_name', "X")
    session['last_name'] = form_data.get('last_name', "last_name")
    session['id'] = form_data.get('student_id', 2324)
    session['count'] = int(session['strawberry'])+int(session['raspberry'])+int(session['apple'])
    now = datetime.datetime.now()
    session['timespan']= now.strftime("%B %d %Y %I:%M %p")
    return redirect('/checkout')

@app.route('/checkout')
def fruits():
    return render_template('checkout.html')

@app.route('/fruits')
def fruits_show():
    return render_template('fruits.html')


@app.route("/count_session")
def count_session():
    # if 'count' in session:
    #     session['count'] += 1
    # else:
    #     session['count'] = 1

    session['count'] = session.get('count', 0) + 1
    return f"Session count {session['count']}"

@app.route("/clear_session")
def clear_session():
    # session.clear() # not recomened 
    session.pop('count', None)
    return {"message": "session count destroyed"}

if __name__=="__main__":   
    app.run(debug=True)