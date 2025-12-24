from flask import Flask, render_template, jsonify

app = Flask(__name__)

# conection

my_dict = {
    "nombre": "jorge",
    "edad": 35,
    "casado": True
}

@app.route("/json")
def json():
    # extraer los datos de la base de datos
    return jsonify(my_dict)

@app.route("/index")
def index():
    # extraer los datos de la base de datos
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/str")
def string():
    return "hola con todos"