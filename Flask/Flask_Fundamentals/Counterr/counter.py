from flask import Flask,render_template,redirect,request,session
app= Flask(__name__)
app.secret_key = 'keep it safe '
@app.route("/")
def index():
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    return render_template('counter.html')


# @app.route("/")    
# def counter():

#     return render_template('counter.html')


@app.route('/destroy')
def destroy_session():
    session.pop('count')
    return redirect('/')



if  __name__== "__main__":
    app.run(debug=True)