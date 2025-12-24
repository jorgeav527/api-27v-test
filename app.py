from flask import Flask, render_template, jsonify

app = Flask(__name__)


my_dict = {
    "nombre": "jorge",
    "edad": 35,
    "casado": True
}

@app.route("/json")
def json():
    return jsonify(my_dict)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/str")
def string():
    return "hola con todos"