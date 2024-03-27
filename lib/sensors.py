import random
from w1thermsensor import W1ThermSensor

class TempSensor:
    def __init__(self, sensor_id):
        self.temp = 0
        self.sensor_id = sensor_id
        self.sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, self.sensor_id)
        print(f"Classe do Sensor de Temperatura DS18B20 criada com ID {self.sensor_id}")
    
    def __updateTemp__(self):
        self.temp = self.sensor.get_temperature()

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
        self.pin = pin
        self.ledStatus = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.__updateLedStatus__()
        print(f"LED criado no pino {self.pin}")

    def __updateLedStatus__(self):
        if self.ledStatus:
            GPIO.output(self.pin, GPIO.HIGH)
        if not self.ledStatus:
            GPIO.output(self.pin, GPIO.LOW)

    def updateLedStatus(self, status):
        self.ledStatus = status
        self.__updateLedStatus__()

    def __del__(self):
        GPIO.cleanup()
        print("GPIO cleanup realizado")


class Fan:
    def __init__(self, pin):
        self.pin = pin
        self.fanStatus = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.__updateFanStatus__()
        print(f"Classe do Ar-Condicionado criada no pin {self.pin}")

    def __updateFanStatus__(self):
        if self.fanStatus:
            GPIO.output(self.pin, GPIO.HIGH)
        if not self.fanStatus:
            GPIO.output(self.pin, GPIO.LOW)

    def updateFanStatus(self, status):
        self.fanStatus = status
        self.__updateFanStatus__()

    def __del__(self):
        GPIO.cleanup()
        print("GPIO cleanup realizado")