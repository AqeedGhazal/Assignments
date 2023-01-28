from flask import Flask,render_template,request 
app = Flask(__name__)
@app.route('/')
def index():
    print(request.form)
    return render_template('form.html',name = "aqeed")
@app.route('/show_info',methods = ['POST'])
def show_info():
    name_from_form=request.form['name']
    location_from_form = request.form['location']
    language_from_form=request.form['language']
    comment_from_form = request.form['comments']
    return render_template('result.html',name_on_template = name_from_form , location_on_template=location_from_form,language_on_template = language_from_form,comments_on_template=comment_from_form)
if __name__ == "__main__":
    app.run(debug=True)