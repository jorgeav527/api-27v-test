from flask import Flask, render_template, jsonify, abort
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

@app.route('/posts', methods=['GET'])
def get_all_post():
    conn = get_db_connection()
    posts_data = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("post/list_post.html", posts=posts_data)

@app.route('/post/<int:post_id>', methods=['GET'])
def get_post_route(post_id):
    conn = get_db_connection()
    post_data = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post_data is None:
        abort(404)
    return render_template('post/post.html', post=post_data)
