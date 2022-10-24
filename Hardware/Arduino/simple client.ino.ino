#include "WiFi.h"

WiFiClient client;
IPAddress server(192,168,4,1);

void setup() {
  // put your setup code here, to run once:
  WiFi.begin("lky2","88643321");
  Serial.begin(115200);
  while (WiFi.status()!=WL_CONNECTED){
    delay(500);
  }
  
  client.connect(server,80);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(WiFi.status());
  Serial.println(WiFi.localIP());

  
  //long RSSI_temp[20];
  //char* RSSI_string[];
  int n = WiFi.scanNetworks(false,false,false,100);
  Serial.println("scan done");
  if (n == 0) {
      Serial.println("no networks found");
  } else {
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i) {
      // Print SSID and RSSI for each network found
    //   for (int j=0;j<2;j++){
    //     if (WiFi.SSID(i)==sta_name[j]){
          Serial.print(WiFi.SSID(i));
          Serial.print(" ("); 
          Serial.print(WiFi.RSSI(i)); 
          Serial.print(")");
          
          
          Serial.println((WiFi.encryptionType(i) == WIFI_AUTH_OPEN)?" ":"*");
    //    }
    //   }
    }
  }

  //Serial.println(WiFi.softAPIP());
  delay(5000);
  client.connect(server,80);

  if (client.connected())
      {
        Serial.println("client connected");
        client.write("123");
        for (int i = 0; i < n; ++i) {
        client.write(WiFi.RSSI(i));
        }
      }
  WiFi.scanDelete();
}
