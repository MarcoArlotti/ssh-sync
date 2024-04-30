import flask
import json
from flask import Flask,request,render_template

app = Flask(__name__)

with open("esercizi_numerati/arlotti_039/arlotti_039.json") as lista_quesiti:
    lista_quesiti = json.load(lista_quesiti)

@app.route("/", methods=["GET", "POST"])
def lista_quesiti(id):
    lista_quesiti = None
    for quesito in lista_quesiti:
        if quesito["id"] == id:
    if lista_quesiti == None:
        return "domanda non trovata \nsuggerimento: (mettere un numero/numero troppo alto)"

    if request.method == "POST":
        
        with open("esercizi_numerati/arlotti_039/arlotti_039.json") as lista_quesiti:
            lista_quesiti = json.load(lista_quesiti)

            risposta_data = request.form.get("risposta_data")
        return 



if __name__ == "__main__":
    app.run(debug=True,port=5069)