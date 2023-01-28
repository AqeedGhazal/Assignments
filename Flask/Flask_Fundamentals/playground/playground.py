from flask import Flask , render_template

app = Flask(__name__)
@app.route('/play')

def view():
    return render_template('index.html')

@app.route('/play/<number_box>')
def block_repeat(number_box):
    repeat = int(number_box)
    return render_template('index2.html',repeat=repeat)

@app.route('/play/<number_box>/<color_change>')
def block_change_color(number_box,color_change):
    repeat = int(number_box)
    colorChange = color_change 
    return render_template('index3.html',repeat=repeat, colorChange=colorChange)


if __name__=="__main__":
    app.run(debug =True)


