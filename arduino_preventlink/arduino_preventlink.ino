#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include "DHT.h"
#include <Thread.h>
#include <ThreadController.h>
Thread hiloDHT=Thread();
const char* ssid     = "familiabonilla";
const char* password = "Lina2014Queen2015Radio2016";
WiFiServer servidorTCP(8266);
WiFiClient clienteTCP;
#define LED D0
#define LED1 D1
#define LED2 D2
#define DHTPIN  D4 // aca conecto el sensor 
#define DHTTYPE DHT11 
#define TIEMPO_SAMPLEO 5000
DHT dht (DHTPIN, DHTTYPE);
ThreadController controladorHilos = ThreadController();
void leeDHT() {
  float hum=dht.readHumidity();
  float temp=dht.readTemperature();
  String datos="temperatura: ";
  datos += temp;
  datos +="\nhumedad: ";
  datos +=hum;
  datos +="\n";
  Serial.print(datos);
  clienteTCP.print(datos);
}

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(LED1,OUTPUT);
  pinMode(LED2,OUTPUT);
  
  Serial.begin(115200);
  delay(100);
  dht.begin();
  
  Serial.print("Conectandose a: ");
  Serial.println(ssid);


  WiFi.begin(ssid, password);  //Intentamos conectarnos a la red Wifi
  
  while (WiFi.status() != WL_CONNECTED) {  //Esperamos hasta que se conecte.
    delay(200);
  }

  Serial.print ("Conectado, IP: ");
  Serial.println (WiFi.localIP());

  servidorTCP.begin();
  hiloDHT.onRun(leeDHT);
  hiloDHT.setInterval(TIEMPO_SAMPLEO);

}

void loop() {

  if (!clienteTCP.connected()) {
        // try to connect to a new client
        clienteTCP = servidorTCP.available();
        if (clienteTCP.connected())
          Serial.println("cliente conectado");
          controladorHilos.add(&hiloDHT);
    }
    else {
        // read data from the connected client
        if (clienteTCP.available() > 0) {
            char dato = clienteTCP.read();
            Serial.write(dato);
            if (dato == '1'){ // led que esta en D0
              digitalWrite(LED, HIGH);
              Serial.write(dato);
            }
            else if (dato == '0'){

              digitalWrite(LED, LOW);
              Serial.write(dato);
            }
            if (dato == '2'){  // aca para el led 1 que esta en d1
              digitalWrite(LED1, HIGH);
              Serial.write(dato);
            }
            else if (dato == '3'){

              digitalWrite(LED1, LOW);
              Serial.write(dato);

            }
            if (dato == '4'){ // aca va el del led2 que esta en D1
              digitalWrite(LED2, HIGH);
              Serial.write(dato);
            }
            else if (dato == '5'){

              digitalWrite(LED2, LOW);
              Serial.write(dato);

              

           
              
        }
    
    }
        controladorHilos.run();
    }

}
