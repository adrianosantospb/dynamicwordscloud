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

# Bibliotecas
from flask import Flask, render_template

# Criando uma instancia WSGI (Web Server Gatwey Interface)
app = Flask('app_autralia_nuvem_de_palavras')

# Rotas 

@app.route('/')
def index():
    return render_template("dynamiccloud.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/create/')
def create():
    return render_template("create.html")



# Roda app
app.run(debug=True, use_reloader=True)