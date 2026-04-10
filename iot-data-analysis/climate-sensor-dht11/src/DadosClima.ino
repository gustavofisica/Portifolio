#include <DHT11.h>

// Definição de constantes
const int DHT11_PIN = 12;    // Pino de dados do DHT11
const int BAUD_RATE = 9600;  // Taxa de comunicação serial
const char MEASURE_COMMAND = '1';  // Comando para iniciar a medição

// Inicializa o sensor DHT11
DHT11 dht11(DHT11_PIN);

// Configuração inicial do Arduino
void setup() {
  Serial.begin(BAUD_RATE);  // Inicia a comunicação serial
  while (!Serial) {
    ;  // Aguarda a inicialização da porta serial
  }
}

// Função para ler e enviar dados do sensor
void readAndSendSensorData() {
  int temperature = 0;
  int humidity = 0;
  int result = dht11.readTemperatureHumidity(temperature, humidity);

  if (result == 0) {
    // Envia a temperatura e umidade para o computador
    Serial.println(temperature);
    Serial.println(humidity);
  } else {
    // Função para lidar com erro do sensor
    handleSensorError(result);
  }
}

// Função para lidar com erros de leitura do sensor
void handleSensorError(int errorCode) {
  Serial.print("Erro no sensor DHT11: ");
  Serial.println(DHT11::getErrorString(errorCode));
}

// Loop principal do Arduino
void loop() {
  if (Serial.available() > 0) {  // Verifica se há dados disponíveis na porta serial
    char command = Serial.read();  // Lê o comando recebido

    if (command == MEASURE_COMMAND) {  // Verifica se o comando é válido
      readAndSendSensorData();  // Lê os dados do sensor e os envia
    } else {
      Serial.println("Comando inválido. Use '1' para medir.");
    }
  }
}
