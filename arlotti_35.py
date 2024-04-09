#https://github.com/angelogalantiscuola/2324_3M/blob/main/7_moduli/esercizio_035.md
import flask
from flask import render_template
import json
from flask import Flask
app = Flask(__name__)

@app.route("/")
def upper_text():
    return "<p>Wealcome to my weather app"
upper_text()

