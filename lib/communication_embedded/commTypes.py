import json

class PacketSensorData:
    def __init__(self):
        self.temp1 = 0
        self.temp2 = 0
        self.presenceSensor = False
    
    def encapsulatePacketSensorData(self):
        encapsulatedPacketSensorData = {
            "temp1": self.temp1,
            "temp2": self.temp2,
            "presenceSensor": self.presenceSensor
        }
        return json.dumps(encapsulatedPacketSensorData)
    
    def decapsulatePacketSensorData(self, encapsulated_data):
        try:
            decoded_data = json.loads(encapsulated_data.decode('utf-8'))
            self.temp1 = decoded_data.get("temp1")
            self.temp2 = decoded_data.get("temp2")
            self.presenceSensor = decoded_data.get("presenceSensor")

        except json.JSONDecodeError as e:
            print("Erro ao decodificar os dados JSON:", e)

    def updatePacketSensorData(self, temp1, temp2, presenceSensor):
        self.temp1 = temp1
        self.temp2 = temp2
        self.presenceSensor = presenceSensor

    def printData(self):
        print("\n----------------------------------")
        print("DADOS DOS SENSORES")
        print(f"Sensor de Presença: {self.presenceSensor}")
        print(f"Sensor de Temp.  1: {self.temp1:.2f}")
        print(f"Sensor de Temp.  2: {self.temp2:.2f}")
        print("----------------------------------\n")

class PacketCommandData:
    def __init__(self):
        self.fan1 = False
        self.fan2 = False
        self.led = False
    
    def updatePacketCommandData(self, fan1, fan2, led):
        self.fan1 = fan1
        self.fan2 = fan2
        self.led = led
    
    def encapsulatePacketCommandData(self):
        encapsulatedPacketSensorData = {
            "fan1": self.fan1,
            "fan2": self.fan2,
            "led": self.led
        }
        return json.dumps(encapsulatedPacketSensorData)

    def decapsulatePacketCommandData(self, encapsulated_data):
        try:
            decoded_data = json.loads(encapsulated_data.decode('utf-8'))
            self.fan1 = decoded_data.get("fan1")
            self.fan2 = decoded_data.get("fan2")
            self.led = decoded_data.get("led")

        except json.JSONDecodeError as e:
            print("Erro ao decodificar os dados JSON:", e)

    def printData(self):
        print("\n----------------------------------")
        print("DADOS DOS COMANDOS")
        print(f"LED       : {self.led}")
        print(f"Ar Cond. 1: {self.fan1}")
        print(f"Ar Cond. 2: {self.fan2}")
        print("----------------------------------\n")