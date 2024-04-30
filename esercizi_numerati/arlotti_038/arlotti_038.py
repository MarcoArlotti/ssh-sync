import flask
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if len(password) < 8:
            return f"la password è troppo corta!"
        return f"username inserito: {username}\n"
    else:
        return render_template("arlotti_038.html")

if __name__ == "__main__":
    app.run(debug=True,port=5069)