import json
from flask import Flask,render_template,request
app = Flask(__name__)

def read_file_json (filename: str):
    with open(filename,"r") as colori_json:
        colors_list = json.load(colori_json)
        return colors_list
    
def update_file_json(filename:str,colors_list:list):
    with open(filename,"w") as colori_json:
        json.dump(colors_list,colori_json,indent=4)

def add_new_user_data(name: str, surname:str, favourites_colors: str,colors_list: list):
    nuova_persona = {
        "name" : name,
        "surname" : surname,
        "favourite_color" : favourites_colors
    }
    colors_list.append(nuova_persona)
    return colors_list

def get_favourites_colors(filename: str) -> list:
    colors_list = read_file_json(filename)
    lista_colori_preferiti = []

    for persona in colors_list:
        colore_preferito = persona["favourite_color"]
        nome = persona["name"]
        cognome = persona["surname"]

        lista_colori_preferiti.append(colore_preferito)

        print(f"alla persona: {nome}\ndi cognome: {cognome}\nha come colore preferito il {colore_preferito}\n\n")
    return lista_colori_preferiti


def get_colors_by_name (filename: str, name: str, surname: str):
    colors_list = read_file_json(filename)
    
    rifai = True
    while rifai == True:
        chi_scelto = str(input("inserire il nome dell'utente chesi vuole ricercare il colore preferito\n"))

        for persona in colors_list:
            nome = persona["name"]

            if nome == chi_scelto:
                favourites_colors = persona["favourite_color"]
                cognome = persona["surname"]
                print("TROVATO")
                rifai = False
                break
    return favourites_colors
    

def CLI_application():
    filename = "verifiche/arlotti_verifica/colors.json"

    colors_list = read_file_json(filename)

    name = str(input("inserire il nome\n"))
    surname = str(input("inserire il cognome\n"))
    favourites_colors = []
    while True:
        colore = str(input("inserire il colore preferito"))
        favourites_colors.append(colore)

        aggiungere_altro = str(input("aggiungere un altro nome?\n\nyes\nno\n"))
        if aggiungere_altro == "no":
            break


    colors_list = add_new_user_data(name,surname,favourites_colors,colors_list)
    update_file_json(filename,colors_list)

    lista_colori_preferiti = get_favourites_colors(filename)

    




#CLI_application()

@app.route("/", methods=["GET", "POST"]) 
def main():
    if request.method == "POST":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        return render_template("add_user_data.html")
    else:
        
    #else:
        

@app.route("/aggiungi_colori")
def aggiunta_colori():
    return render_template("aggiungi_colori.html")




if __name__ == "__main__":
    
        app.run(debug=True, port=5069)