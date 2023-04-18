#include <WiFi.h>
#include <WebSocketsServer.h>
#include "ArduinoJson.h"
#include "stdio.h"
#include "stdint.h"

// Constants
const char* ssid = "lky";
const char* password = "88643321";

// Globals
WebSocketsServer webSocket = WebSocketsServer(80);

//Json declare
StaticJsonDocument<800> Jsonfile;
JsonObject root = Jsonfile.createNestedObject();
JsonObject rec_AP1 = Jsonfile.createNestedObject();
JsonObject rec_AP2 = Jsonfile.createNestedObject();
JsonObject rec_AP3 = Jsonfile.createNestedObject();
JsonObject rec_AP4 = Jsonfile.createNestedObject();
JsonObject rec_AP5 = Jsonfile.createNestedObject();
JsonObject rec_AP6 = Jsonfile.createNestedObject();
JsonObject rec_AP7 = Jsonfile.createNestedObject();
JsonObject rec_AP8 = Jsonfile.createNestedObject();
JsonObject rec_AP9 = Jsonfile.createNestedObject();
JsonObject rec_AP10 = Jsonfile.createNestedObject();
JsonObject rec_AP11 = Jsonfile.createNestedObject();
JsonObject rec_AP12 = Jsonfile.createNestedObject();
JsonObject rec_AP13 = Jsonfile.createNestedObject();
JsonObject rec_AP14 = Jsonfile.createNestedObject();
JsonObject rec_AP15 = Jsonfile.createNestedObject();


// Called when receiving any WebSocket message
void onWebSocketEvent(uint8_t num,
                      WStype_t type,
                      uint8_t * payload,
                      size_t length) {

  // Figure out the type of WebSocket event
  switch(type) {

    // Client has disconnected
    case WStype_DISCONNECTED:
      Serial.printf("[%u] Disconnected!\n", num);
      break;

    // New client has connected
    case WStype_CONNECTED:
      {
        IPAddress ip = webSocket.remoteIP(num);
        Serial.printf("[%u] Connection from ", num);
        Serial.println(ip.toString());
      }
      break;

    // Echo text message back to client
    case WStype_TEXT:
    {
      int n = WiFi.scanNetworks(false,false,false,100);
      Serial.println("scan done");
      if (n == 0) {
        Serial.println("no networks found");
      } else {
        Serial.print(n);
        Serial.println(" networks found");
        for (int i = 0; i < n; ++i) {
          // Print SSID and RSSI for each network found
          for (int j = 1; j<=16;++j){
            if (WiFi.SSID(i)==Jsonfile[j]["AP name"]){
              Serial.print(WiFi.SSID(i));
              Serial.print(WiFi.RSSI(i));
              Serial.println("checked ");
              Jsonfile[j]["RSSI"]=WiFi.RSSI(i);
            }
          }
        }
      }
      String json;
      serializeJson(Jsonfile,json);
      Serial.printf("[%u] Text: %s\n", num, json);
      webSocket.sendTXT(num, json);
      break;
    }
    // For everything else: do nothing
    case WStype_BIN:
    case WStype_ERROR:
    case WStype_FRAGMENT_TEXT_START:
    case WStype_FRAGMENT_BIN_START:
    case WStype_FRAGMENT:
    case WStype_FRAGMENT_FIN:
    default:
      break;
  }
}

void setup() {

  // Start Serial port
  Serial.begin(115200);

  // Connect to access point
  WiFi.mode(WIFI_MODE_APSTA);
  Serial.println("Connecting");
  WiFi.begin(ssid, password);
  while ( WiFi.status() != WL_CONNECTED ) {
    delay(500);
    Serial.print(".");
  }

  // Print our IP address
  Serial.println("Connected!");
  Serial.print("My IP address: ");
  Serial.println(WiFi.localIP());

  // Start WebSocket server and assign callback
  webSocket.begin();
  webSocket.onEvent(onWebSocketEvent);

  //initialise the json file
  root["Station name"]="AP6";
  rec_AP1["AP name"]="AP1";
  rec_AP2["AP name"]="AP2";
  rec_AP3["AP name"]="AP3";
  rec_AP4["AP name"]="AP4";
  rec_AP5["AP name"]="AP5";
  rec_AP6["AP name"]="AP7";
  rec_AP7["AP name"]="AP8";
  rec_AP8["AP name"]="AP9";
  rec_AP9["AP name"]="AP10";
  rec_AP10["AP name"]="AP11";
  rec_AP11["AP name"]="AP12";
  rec_AP12["AP name"]="AP13";
  rec_AP13["AP name"]="AP14";
  rec_AP14["AP name"]="AP15";
  rec_AP15["AP name"]="AP16";

  WiFi.softAP("AP6");
}

void loop() {

  // Look for and handle WebSocket data
  webSocket.loop();
}