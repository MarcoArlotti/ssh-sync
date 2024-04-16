import flask
from flask import Flask
import json
#python -m flask --app  Sanchi_035.py run --port 5002 
with open("esercizi_numerati/arlotti_036/arlotti_036.json","r") as lista_alunni:
    lista_alunni = json.load(lista_alunni)

app = Flask(__name__)

@app.route("/")
def mostra_voti(lista_alunni):
    return lista_alunni