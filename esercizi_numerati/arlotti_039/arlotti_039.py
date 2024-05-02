import flask
import json
from flask import Flask,request,render_template

app = Flask(__name__)

def read_flashcards(filename: str) -> None:
    with open(filename, "r") as file_json:
        lista_domande = json.load(file_json)
        return lista_domande
    
def get_flashcard_by_id(id: int,lista_domande) -> None:
    for domanda in lista_domande:
        id_ = domanda["id"]
        if id_ == id:
            domanda = domanda["question"]
            print(domanda)

def prompt_for_id() -> int:
    rifai = True
    while rifai == True:
        rifai = False
        id_scelto = input("inserire l'id della domanda che si vuole visulizzare")
        try:
            id_scelto = int(id_scelto)
        except:
            rifai = True
    return id_scelto

def get_flashcard_by_id(id_scelto):

    for domanda in lista_domande:
        id = domanda["id"]
        if id_scelto == id:
            print(domanda["question"])
            break
    return lista_domande




if __name__ == "__main__":
    #app.run(debug=True,port=5069)
    filename = "esercizi_numerati/arlotti_039/arlotti_039.json"
    lista_domande = read_flashcards(filename)
    id = 2
    get_flashcard_by_id(id,lista_domande)
    id_scelto = prompt_for_id()
    get_flashcard_by_id(id_scelto)
    print(lista_domande)
