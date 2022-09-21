from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ('', 62345)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()