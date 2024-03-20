import random


class TempSensor:
    def __init__(self, pin):
        self.pin = pin
        self.temp = 0
        print(f"Classe do Sensor de Temperatura DS18B20 criada no pin {self.pin}")
    
    def __updateTemp__(self):
        self.temp = random.uniform(30,40)

    def getTemp(self):
        self.__updateTemp__()
        return self.temp
    
class PresenceSensor:
    def __init__(self, pin):
        self.pin = pin
        self.presence = 0
        print(f"Classe do Sensor de Presença criada no pin {self.pin}")
    
    def __updatePresence__(self):
        self.presence = random.choice([False, True])
    
    def getPresenceInfo(self):
        self.__updatePresence__()
        return self.presence

class LED:
    def __init__(self, pin):
        print("criado")


class Fan:
    def __init__(self, pin):
        self.pin = pin
        self.fanStatus = False
        print(f"Classe do Ar-Condicionado criada no pin {self.pin}")
    
    def __updateFanStatus__(self, status):
        self.fanStatus = status
    
    def turnOn(self):
        self.__updateFanStatus__(True)
        return True
    def turnOff(self):
        self.__updateFanStatus__(False)
        return False