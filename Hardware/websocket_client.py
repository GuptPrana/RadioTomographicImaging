import websocket
import simplejson
from _datetime import datetime
import time



# batch 1
start_time = datetime.now()
print(start_time.strftime("%M%S"))
# Connect to WebSocket server
ws1 = websocket.WebSocket()
ws2 = websocket.WebSocket()
ws3 = websocket.WebSocket()
ws4 = websocket.WebSocket()
ws5 = websocket.WebSocket()

# use the router to hard code the IP address of the ESP32
ws1.connect("ws://192.168.28.180")
ws2.connect("ws://192.168.28.137")
ws3.connect("ws://192.168.29.80")
ws4.connect("ws://192.168.45.105")
ws5.connect("ws://192.168.28.105")
print("1st side")

# trigger the ESP32
ws1.send("hello")
ws2.send("hello")
ws3.send("hello")
ws4.send("hello")
ws5.send("hello")

# Wait for server to respond and print it
result1 = ws1.recv()
# print("Received: " + result1)
batch1 = simplejson.loads(result1)

result2 = ws2.recv()
# print("Received: " + result2)
data2 = simplejson.loads(result2)
batch1.append(data2)

result3 = ws3.recv()
# print("Received: " + result2)
data3 = simplejson.loads(result3)
batch1.append(data3)

result4 = ws4.recv()
# print("Received: " + result2)
data4 = simplejson.loads(result4)
batch1.append(data4)

result5 = ws5.recv()
# print("Received: " + result2)
data5 = simplejson.loads(result5)
batch1.append(data5)

# Gracefully close WebSocket connection
ws1.close()
ws2.close()
ws3.close()
ws4.close()
ws5.close()

# batch 2
time.sleep(1)
right_time = datetime.now()
print(right_time.strftime("%M%S"))
# Connect to WebSocket server
ws6 = websocket.WebSocket()
ws7 = websocket.WebSocket()
ws8 = websocket.WebSocket()


# use the router to hard code the IP address of the ESP32
ws6.connect("ws://192.168.28.232")
ws7.connect("ws://192.168.28.242")
ws8.connect("ws://192.168.29.29")
print("2nd side")

# trigger the ESP32
ws6.send("hello")
ws7.send("hello")
ws8.send("hello")

# Wait for server to respond and print it
result6 = ws6.recv()
# print("Received: " + result1)
batch2 = simplejson.loads(result6)

result7 = ws7.recv()
# print("Received: " + result2)
data7 = simplejson.loads(result7)
batch2.append(data7)

result8 = ws8.recv()
# print("Received: " + result2)
data8 = simplejson.loads(result8)
batch2.append(data8)


# Gracefully close WebSocket connection
ws6.close()
ws7.close()
ws8.close()

# batch 3
time.sleep(1)
opp_time = datetime.now()
print(opp_time.strftime("%M%S"))
# Connect to WebSocket server
ws9 = websocket.WebSocket()
ws10 = websocket.WebSocket()
ws11 = websocket.WebSocket()
ws12 = websocket.WebSocket()
ws13 = websocket.WebSocket()

# use the router to hard code the IP address of the ESP32
ws9.connect("ws://192.168.29.53")
ws10.connect("ws://192.168.29.67")
ws11.connect("ws://192.168.28.136")
ws12.connect("ws://192.168.29.23")
ws13.connect("ws://192.168.66.247")
print("3rd side")

# trigger the ESP32
ws9.send("hello")
ws10.send("hello")
ws11.send("hello")
ws12.send("hello")
ws13.send("hello")

# Wait for server to respond and print it
result9 = ws9.recv()
# print("Received: " + result1)
batch3 = simplejson.loads(result9)

result10 = ws10.recv()
# print("Received: " + result2)
data10 = simplejson.loads(result10)
batch3.append(data10)

result11 = ws11.recv()
# print("Received: " + result2)
data11 = simplejson.loads(result11)
batch3.append(data11)

result12 = ws12.recv()
# print("Received: " + result2)
data12 = simplejson.loads(result12)
batch3.append(data12)

result13 = ws13.recv()
# print("Received: " + result2)
data13 = simplejson.loads(result13)
batch3.append(data13)

# Gracefully close WebSocket connection
ws9.close()
ws10.close()
ws11.close()
ws12.close()
ws13.close()

# batch 4
time.sleep(1)
left_time = datetime.now()
print(left_time.strftime("%M%S"))
# Connect to WebSocket server
ws14 = websocket.WebSocket()
ws15 = websocket.WebSocket()
ws16 = websocket.WebSocket()


# use the router to hard code the IP address of the ESP32
ws14.connect("ws://192.168.28.164")
ws15.connect("ws://192.168.66.228")
ws16.connect("ws://192.168.30.190")
print("4th side")

# trigger the ESP32
ws14.send("hello")
ws15.send("hello")
ws16.send("hello")

# Wait for server to respond and print it
result14 = ws14.recv()
# print("Received: " + result1)
batch4 = simplejson.loads(result14)

result15 = ws15.recv()
# print("Received: " + result2)
data15 = simplejson.loads(result15)
batch4.append(data15)

result16 = ws16.recv()
# print("Received: " + result2)
data16 = simplejson.loads(result16)
batch4.append(data16)


# Gracefully close WebSocket connection
ws14.close()
ws15.close()
ws16.close()

# combine and output
print(batch1)
print(batch2)
print(batch3)
print(batch4)
batch1.append(batch2)
batch1.append(batch3)
batch1.append(batch4)
print(batch1)
curr_time = datetime.now()
filename = curr_time.strftime("%m%d-%H%M%S")
print(curr_time.strftime("%M%S"))
with open("%s.json" % filename, "w") as outfile:
    simplejson.dump(batch1, outfile, indent=2)
