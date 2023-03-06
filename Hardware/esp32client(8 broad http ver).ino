#include "WiFi.h"
#include "ArduinoJson.h"
#include "stdio.h"
#include "stdint.h"
#include "HTTPClient.h"


WiFiClient client;
const char* serverName = "http://192.168.59.4:8000";
unsigned long last_time=0;
HTTPClient http;

StaticJsonDocument<400> Jsonfile;
JsonObject root = Jsonfile.createNestedObject();
JsonObject rec_AP1 = Jsonfile.createNestedObject();
JsonObject rec_AP2 = Jsonfile.createNestedObject();
JsonObject rec_AP3 = Jsonfile.createNestedObject();
JsonObject rec_AP4 = Jsonfile.createNestedObject();
JsonObject rec_AP5 = Jsonfile.createNestedObject();
JsonObject rec_AP6 = Jsonfile.createNestedObject();
JsonObject rec_AP7 = Jsonfile.createNestedObject();

void setup() {
  //setup as APSTA mode
  WiFi.mode(WIFI_MODE_APSTA);
  WiFi.begin("lky","88643321");
  Serial.begin(115200);
  while (WiFi.status()!=WL_CONNECTED){
    delay(500);
  }
  Serial.println("connection finished");
  //initialise the json file
  root["Station name"]="lky1";
  rec_AP1["AP name"]="lky2";
  rec_AP2["AP name"]="lky3";
  rec_AP3["AP name"]="lky4";
  rec_AP4["AP name"]="lky5";
  rec_AP5["AP name"]="lky6";
  rec_AP6["AP name"]="lky7";
  rec_AP7["AP name"]="lky8";
  
}

void loop() {
  if ((millis()-last_time)==6000){
    //WiFi.begin("lky","88643321");
  }
  if ((millis()-last_time)>10000){
    // put your main code here, to run repeatedly:
    //Serial.println(WiFi.localIP());
    //Serial.print("time is ");
    //Serial.println(millis());
    http.begin(client,serverName);
    if (http.connected()){Serial.println("Http connected");}

    //Serial.print("time is ");
    //Serial.println(millis());

    int n = WiFi.scanNetworks(false,false,false,100);
    Serial.println("scan done");
    if (n == 0) {
        Serial.println("no networks found");
    } else {
      Serial.print(n);
      Serial.println(" networks found");
      for (int i = 0; i < n; ++i) {
        // Print SSID and RSSI for each network found
          for (int j = 1; j<=8;++j){
            if (WiFi.SSID(i)==Jsonfile[j]["AP name"]){
              Serial.print(WiFi.SSID(i));
              Serial.print(WiFi.RSSI(i));
              Serial.println("checked ");
              Jsonfile[j]["RSSI"]=WiFi.RSSI(i);
            }
          }
      }
    }

    Serial.print("time is ");
    Serial.println(millis());

    http.addHeader("Content-Type", "application/json");
    String json;
    serializeJson(Jsonfile,json);
    serializeJson(Jsonfile,Serial);
    int httpResponseCode = http.POST(json);
    Serial.println(httpResponseCode);
    //delay(5000);
    //http.disconnect(true);
    Serial.println("");
    Serial.println("");
    
    WiFi.scanDelete();

    WiFi.softAP("lky1","88643321");

    last_time=millis();
  }
}
