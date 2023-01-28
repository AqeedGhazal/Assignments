
from flask import Flask , render_template 
app = Flask(__name__)
@app.route('/<x>/<y>')
def display(x,y):
    input1=int(x)
    input2=int(y)
    return render_template('checkboard1.html',input1=input1,input2=input2)

if __name__ == "__main__":
    app.run (debug=True)