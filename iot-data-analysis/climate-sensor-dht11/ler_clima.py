import serial
import time
from datetime import datetime

# Configuração da porta serial (Substitua 'COM3' pela sua porta serial)
SERIAL_PORT = 'COM10'  # Exemplo: 'COM3' para Windows ou '/dev/ttyUSB0' para Linux
BAUD_RATE = 9600
COMMAND = '1'  # Comando para solicitar dados ao Arduino
INTERVAL = 600  # Intervalo de 10 minutos em segundos
FILE_NAME = 'dados_dht11.txt'

def init_serial_connection(port, baud_rate):
    """Inicializa a conexão serial."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Conectado ao {port} a {baud_rate} bps.")
        time.sleep(2)  # Aguarda o Arduino reiniciar após a conexão
        return ser
    except serial.SerialException as e:
        print(f"Erro ao conectar na porta {port}: {e}")
        return None

def send_command(ser, command):
    """Envia um comando ao Arduino."""
    ser.write(command.encode())  # Envia o comando como bytes
    print(f"Comando '{command}' enviado ao Arduino.")

def read_data(ser):
    """Lê os dados de temperatura e umidade da porta serial."""
    try:
        # Lê as duas linhas de dados: temperatura e umidade
        temperature = ser.readline().decode().strip()  # Lê e decodifica a linha de dados de temperatura
        humidity = ser.readline().decode().strip()  # Lê e decodifica a linha de dados de umidade
        return temperature, humidity
    except serial.SerialException as e:
        print(f"Erro ao ler dados: {e}")
        return None, None

def save_data_to_file(file_name, temperature, humidity):
    """Salva os dados de temperatura e umidade em uma única linha em um arquivo de texto com data e horário."""
    with open(file_name, 'a') as file:
        # Obtem a data e o horário atuais
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Escreve os dados no arquivo com o timestamp
        file.write(f"{timestamp} - Temperature: {temperature}, Humidity: {humidity}\n")
        print(f"Dados salvos: {timestamp} - Temperature: {temperature} °C, Humidity: {humidity} %")

def main():
    # Inicializa a conexão serial
    ser = init_serial_connection(SERIAL_PORT, BAUD_RATE)
    
    if not ser:
        print("Falha na conexão serial. Encerrando programa.")
        return

    while True:
        # Envia o comando para o Arduino
        send_command(ser, COMMAND)

        # Aguarda um pouco para garantir que os dados estejam prontos
        time.sleep(2)

        # Lê a resposta do Arduino
        temperature, humidity = read_data(ser)
        if temperature and humidity:
            print(f"Dados recebidos do Arduino: Temperature: {temperature}, Humidity: {humidity}")
            # Salva os dados no arquivo de texto
            save_data_to_file(FILE_NAME, temperature, humidity)
        else:
            print("Nenhum dado recebido ou erro de leitura.")

        # Aguarda o intervalo definido antes de enviar o próximo comando
        print(f"Aguardando {INTERVAL / 3600} horas para o próximo comando.")
        time.sleep(INTERVAL)

    # Fecha a conexão serial ao finalizar (nunca será alcançado no loop infinito)
    ser.close()

if __name__ == "__main__":
    main()
