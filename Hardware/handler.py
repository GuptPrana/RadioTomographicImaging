from http.server import HTTPServer, BaseHTTPRequestHandler
import simplejson

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 response
        self.send_response(200)
        # send response headers
        self.end_headers()
        # send the body of the response
        self.wfile.write(bytes("It Works!", "utf-8"))

    def do_POST(self):
        # read the content-length header
        content_length = int(self.headers.get("Content-Length"))
        # read that many bytes from the body of the request
        body = self.rfile.read(content_length)
        data =simplejson.loads(body)
        with open("test.json","w") as outfile:
            simplejson.dump(data,outfile)
        print "{}".format(data)
        self.send_response(200)
        self.end_headers()
        # echo the body in the response
        self.wfile.write(body)

httpd = HTTPServer(('localhost', 8000), MyHandler)
httpd.serve_forever()