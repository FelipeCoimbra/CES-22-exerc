#!/usr/bin/env python

from flask import Flask, render_template
from flask_socketio import SocketIO

app  = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('send msg')
def handle_message_rec(json, methods=["GET","POST"]):
    print("Received 'send msg' : " + str(json) )
    socketio.emit("update", json, callback=message_received)

def message_received(methods=["GET", "POST"]):
    pass


if __name__ == "__main__":
    socketio.run(app, debug=True)
