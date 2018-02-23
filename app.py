# Katrin Terton's Words Cloud App
# Developed by Adriano Santos (br.linkedin.com/in/adrianosantospb)
#
# Technologies
#
# Python 3.6 - https://www.python.org/
# Flask - http://flask.pocoo.org/docs/0.12/tutorial/
# D3 - https://d3js.org
# Bootstrap - https://getbootstrap.com/
# ResponsiveVoice - https://responsivevoice.org/
# This app was inspired in https://github.com/jasondavies/d3-cloud
# This app was inspired in Ash Blue (https://codepen.io/ashblue/pen/mCtuA)
# This app was inspired in Luke Reid (https://codepen.io/lukeandrewreid/pen/OVPGXN)





# Bibliotecas
from flask import Flask, request, render_template


import util


# Criando uma instancia WSGI (Web Server Gatwey Interface)
app = Flask('app_autralia_nuvem_de_palavras')

# Rotas 

@app.route('/')
def index():
    return render_template("dynamiccloud.html")

@app.route('/')
@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/visitor/')
def visitor():

    return render_template("visitor.html")

#@app.route('/admin/')
#def admin():
    #return render_template("admin.html")

@app.route('/visitor/', methods=['POST'])
def my_form_post():

    first = request.form['first_word']
    second = request.form['second_word']
    third = request.form['third_word']
    util.add_word([first, second, third])
    return render_template("success.html")

@app.route('/admin/')
def admin():
    return render_template('admin.html', words=util.read_json()["words"])


@app.route('/admin/', methods=['POST'])
def save_updates():
    json_table = request.form['inpt']
    util.save_updates(json_table)
    return render_template('admin.html', words=util.read_json()["words"])

# Roda app
app.run(debug=True, use_reloader=True)