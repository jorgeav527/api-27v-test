from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/ws')
def index():
    return render_template('ws.html')

@socketio.on('connect')
def handle_connect():
    print('Servidor: Cliente conectado')

@socketio.on('message')
def handleMessage(msg):
    print(f'Mensaje de cliente: {msg}')
    send(f"Echo del servidor {msg}", broadcast=True, include_self=False)