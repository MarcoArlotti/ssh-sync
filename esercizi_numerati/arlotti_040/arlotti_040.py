import json
from flask import Flask, render_template
filename = "esercizi_numerati/arlotti_040/arlotti_040.json"
app = Flask(__name__)
@app.route("/")
def link():
    return render_template('arlotti_040.html', link=link)

@app.route('/recipes')
def recipes():
    filename = "esercizi_numerati/arlotti_040/arlotti_040.json"
    ricette = read_recipes(filename)
    return render_template("pagina_ricette.html", ricette=ricette)

@app.route('/recipe/<int:id>')
def recipe(id):
    recipe = get_recipe_by_id(id)
    return render_template('recipe.html', recipe=recipe)



def read_recipes(filename: str) -> None:
    with open(filename,"r") as file_json:
        ricette = json.load(file_json)
    return ricette

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
        recipes = json.load(file_json)

    for ricetta in recipes:
        id_ricetta = ricetta["id"]
        if id_ricetta == id:
            print(ricetta)
            break
    return ricetta
            




if __name__ == "__main__":
    app.run(debug=True, port=5069)
