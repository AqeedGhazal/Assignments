from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello():
    print('/')
    return " Hello World ! "

@app.route('/dojo')
def hello_dojo():
    return " Dojo!"

@app.route('/say/<name>')
def hello_person(name):
    return f"Hi {name}!" 

@app.route('/repeat/<int:num>/<name>')
def repeat(name,num):
    return f'{name} ' * num

if __name__== "__main__":
    app.run(debug=True)