import flask
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/", methods=["get","post"])
def login():
    if request.method == "post":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"username inserito:{username}\npassword:{password}"
    else:
        return render_template("arlotti_038.html")

if __name__ == "__main__":
    app.run(debug=True,port=5069)