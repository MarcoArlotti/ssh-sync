from flask import Flask,render_template
import json
app = Flask(__name__)

@app.route("/")
def mostra_link():
    with open("esercizi_numerati/arlotti_037/arlotti_037.json","r") as lista_link:
        lista_link = json.load(lista_link)
        # return render_template("esercizi_numerati/arlotti_037/templates/arlotti_037.html",lista_link=lista_link)
        return render_template("arlotti_037.html",lista_link=lista_link)
    