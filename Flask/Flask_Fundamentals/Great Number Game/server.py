from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
app.secret_key = "guess game "

@app.route('/')
def guess_game():
    guess_number = random.randrange(1,100)
    session['guess']= guess_number
    return render_template('index.html')
@app.route('/check' , methods =['POST'])
def check_value():
    input_value = int(request.form['input_guess'])
    random_guess = session['guess']
    box_color = ""
    message = ""
    rest_buttn = ""
    message2 = ""


    if input_value : 

        if input_value >random_guess:
            box_color = "red"
            message = " Too High !"
            return render_template('index.html' ,box_color = box_color , message = message)
        
        elif input_value < random_guess:
            box_color = "blue"
            message = " Too low !"
            return render_template('index.html' ,box_color = box_color , message = message )

        else:
            box_color = "green"
            message = f" Good Job ! {session['guess']} was the number "
            rest_buttn = Markup('<a href="/"> <button type="submit">Play Again </button></a>')
            session.clear()
    return render_template('index.html' , box_color = box_color , message = message , rest_buttn=rest_buttn)

if __name__=="__main__":
    
    app.run(debug=True) 