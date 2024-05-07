import json
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def link():
    return render_template('arlotti_040.html', recipe=recipe)

@app.route('/recipe/<int:id>')
def recipe(id):
    recipe = get_recipe_by_id(id)
    return render_template('arlotti_040.html', recipe=recipe)

def read_recipes(filename: str) -> None:
    with open(filename,"r") as file_json:
        ricette = json.load(file_json)

def prompt_for_id() -> int:
    id = input("inserire un id")
    rifai = True
    while rifai == True:
        rifai = False
        try:
            id = int(id)
        except:
            print("rifai inserendo un valore corretto")
            rifai = True
    return id

def get_recipe_by_id(id: int) -> None:
    with open(filename,"r") as file_json:
        ricette = json.load(file_json)

    for ricetta in ricette:
        id_ricetta = ricetta["id"]
        if id_ricetta == id:
            print(ricetta)
            break
    return ricetta
            



filename = "esercizi_numerati/arlotti_040/arlotti_040.json"

if __name__ == "__main__":
    app.run(debug=True, port=5069)
