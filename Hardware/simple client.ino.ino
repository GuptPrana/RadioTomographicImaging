#include "WiFi.h"
#include "ArduinoJson.h"
#include "stdio.h"
#include "stdint.h"
#include "HTTPClient.h"

StaticJsonDocument<200> Jsonfile;
WiFiClient client;
const char* serverName = "http://192.168.235.4:8000";
IPAddress server(192,168,4,1);
unsigned long last_time=0;
HTTPClient http;

JsonObject root = Jsonfile.createNestedObject();
JsonObject rec_AP1 = Jsonfile.createNestedObject();

void setup() {
  // put your setup code here, to run once:
  WiFi.begin("lky","88643321");
  Serial.begin(115200);
  while (WiFi.status()!=WL_CONNECTED){
    delay(500);
  }
  Serial.println("connection finished");
  //client.connect(server,80);
  root["Station name"]="lky1";
  rec_AP1["AP name"]="lky2";
  //serializeJson(rec_AP1["AP name"], Serial);

}

void loop() {
  if ((millis()-last_time)>10000){
    // put your main code here, to run repeatedly:
    //Serial.println(WiFi.status());
    Serial.println(WiFi.localIP());
    http.begin(client,serverName);
    //char* RSSI_string[];
    int n = WiFi.scanNetworks(false,false,false,100);
    Serial.println("scan done");
    if (n == 0) {
        Serial.println("no networks found");
    } else {
      //Serial.println(rec_AP1["AP name"].as<String>());
      //serializeJson(rec_AP1["AP name"], Serial);
      Serial.print(n);
      Serial.println(" networks found");
      
      for (int i = 0; i < n; ++i) {
        // Print SSID and RSSI for each network found
      //   for (int j=0;j<2;j++){
      //     if (WiFi.SSID(i)==sta_name[j]){
            if (WiFi.SSID(i)==Jsonfile[1]["AP name"]){
              Serial.print("checked ");
              rec_AP1["RSSI"]=WiFi.RSSI(i);
            }
            Serial.print(WiFi.SSID(i));
            Serial.print(" (");  
            Serial.print(WiFi.RSSI(i));
            Serial.print(")");
            Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");
            
      //    }
      //   }
      }
    }
    //serializeJson(rec_AP1, Serial);
    http.addHeader("Content-Type", "application/json");
    String json;
    serializeJson(Jsonfile,json);
    serializeJson(Jsonfile,Serial);
    int httpResponseCode = http.POST(json);
    //Serial.println(WiFi.softAPIP());
    //delay(5000);
    
    WiFi.scanDelete();

    last_time=millis();
  }
}
