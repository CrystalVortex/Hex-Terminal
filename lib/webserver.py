import os
from http.server import HTTPServer, CGIHTTPRequestHandler

def start():
    os.chdir('.')
    print("Warning: Starting the web server will not allow you to exit until you do ctrl + C")
    server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
    print("Started on port 80... (localhost)")
    server_object.serve_forever()
