import SimpleHTTPServer
import SocketServer
import os
import socket

# minimal web server.  serves files relative to the
# current directory.

PORT = 8080
local_hostname = os.getenv("OPENSHIFT_PLAY2_IP")

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer((socket.gethostbyname (local_hostname), PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

