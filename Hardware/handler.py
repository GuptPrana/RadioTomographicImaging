from http.server import HTTPServer, BaseHTTPRequestHandler ,SimpleHTTPRequestHandler
import simplejson


class MyHandler(SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        # read the content-length header
        content_length = int(self.headers.get("Content-Length"))
        # read that many bytes from the body of the request
        body = self.rfile.read(content_length)
        with open("test.json", "r") as infile:
            original_data = simplejson.load(infile)
        new_data = simplejson.loads(body)
        original_data.append(new_data)
        with open("test.json", "w") as outfile:
            simplejson.dump(original_data, outfile, indent=2)
        print("{}".format(original_data))

        self.send_response(200)
        self.end_headers()
        # echo the body in the response
        self.wfile.write(body)


host = ''
port = 8000
httpd = HTTPServer((host, port), MyHandler).serve_forever()
