import os
import socket
from excuse_me import app

port = int(os.environ.get('PORT', 33508))
# hostname = socket.gethostname()
app.run(host='0.0.0.0', port=port)
