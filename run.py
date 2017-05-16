import socket

from excuse_me import app

hostname = socket.gethostname()
app.run('127.0.0.1', port=5001)
