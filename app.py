from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

my_dict = {
    "nombre": "jorge",
    "edad": 35,
    "casado": True
}

@app.route("/json")
def json():
    # extraer los datos de la base de datos
    return jsonify(my_dict)

@app.route("/str")
def string():
    return "hola con todos"

@app.route("/")
def base():
    # extraer los datos de la base de datos
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/post', methods=['GET'])
def get_all_post():
    conn = get_db_connection()
    posts_data = conn.execute('SELECT * FROM posts').fetchall()
    return render_template("post/list_post.html", posts=posts_data)