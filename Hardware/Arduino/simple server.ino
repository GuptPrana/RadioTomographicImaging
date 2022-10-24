#include "WiFi.h"
WiFiServer server(80);
WiFiClient client;

void setup() {
  // put your setup code here, to run once:
  WiFi.softAP("lky2","88643321");
  Serial.begin(115200);
  delay(5000);
  server.begin();
  IPAddress myAddress = WiFi.localIP();
  Serial.println(myAddress);
}

void loop() {
  // listen for incoming clients
  //Serial.println("scan");
  WiFiClient client = server.available();
  if (client) {

    if (client.connected()) {
      Serial.println("Connected to client");
      String c =client.readString();
      Serial.println(c);
      Serial.println("");
    }

    // close the connection:
    client.stop();
  }
}
