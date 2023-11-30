#include <DHT.h>

#define DHT_TYPE DHT11
#define DHT_PIN_1 13
#define DHT_PIN_2 11
#define DHT_PIN_3 9

DHT dht1(DHT_PIN_1, DHT_TYPE);
DHT dht2(DHT_PIN_2, DHT_TYPE);
DHT dht3(DHT_PIN_3, DHT_TYPE);

void setup() {
  Serial.begin(9600);
  
  dht1.begin();
  dht2.begin();
  dht3.begin();
}

void loop() {
  delay(2000);

  float humidity1 = dht1.readHumidity();
  float temperatureC1 = dht1.readTemperature();

  float humidity2 = dht2.readHumidity();
  float temperatureC2 = dht2.readTemperature();

  float humidity3 = dht3.readHumidity();
  float temperatureC3 = dht3.readTemperature();

  if (isnan(humidity1) || isnan(temperatureC1) ||
      isnan(humidity2) || isnan(temperatureC2) ||
      isnan(humidity3) || isnan(temperatureC3)) {
    Serial.println("Failed to read from one of the DHT sensors!");
    return;
  }

  Serial.print(humidity1);
  Serial.print(",");
  Serial.println(temperatureC1);

  Serial.print(humidity2);
  Serial.print(",");
  Serial.println(temperatureC2);

  Serial.print(humidity3);
  Serial.print(",");
  Serial.println(temperatureC3);
}