from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import simplejson
import websocket
import rel
from _datetime import datetime


def on_message(ws, message):
    print(message)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_error(ws, error):
    print(error)


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
            AP = []
        new_data = simplejson.loads(body)

        if new_data[0]['Station name'] not in original_data:
            print(new_data)
            print(new_data[0]['Station name'])
            print(original_data)
            original_data.append(new_data)

        original_data.sort(key=lambda x: x[0]['Station name'])
        if len(original_data) == 16:
            curr_time = datetime.now()
            filename = curr_time.strftime("%m%d-%H%M%S")
            with open("%s.json" % filename, "w") as outfile:
                simplejson.dump(original_data, outfile, indent=2)
            with open("test.json", "w") as clearfile:
                simplejson.dump([], clearfile)
            # print("{}".format(original_data))
        else:
            with open("test.json", "w") as outfile:
                simplejson.dump(original_data, outfile, indent=2)
            # print("{}".format(original_data))
            print(len(original_data))
        self.send_response(200)
        self.end_headers()
        # echo the body in the response
        self.wfile.write(body)

    # with open("test.json", "r") as infile:
    #     original_data = simplejson.load(infile)
    # if len(original_data) != 0:
    #     simplejson.dump([], infile)
host = ''
port = 80
# httpd = HTTPServer((host, port), MyHandler).serve_forever()
ws = websocket.WebSocket()
ws.connect("ws://192.168.208.113")
print("Connected to WebSocket server")
ws.send("hello")
# ws = websocket.WebSocketApp("wss://192.168.208.113", on_message=on_message, on_close=on_close,on_error=on_error)
# ws.run_forever(dispatcher=rel, reconnect=5)
# rel.signal(2, rel.abort)
# rel.dispatch()
