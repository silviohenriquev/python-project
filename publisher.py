import paho.mqtt.client as mqtt
from lib.sensors import *
from lib.communication_embedded.MQTTEMQXCommunication import MQTTEMQXCommunication
from lib.communication_embedded.commTypes import *
from lib.communication_embedded.commConfig import *
from time import sleep, time

deviceFunction = "publisher"
deviceId = "testeclasse"
timeStep = 3

led = LED(4)
fan1 = Fan(17)
fan2 = Fan(18)
tempSensor1 = TempSensor("28-00000abcdeff")
tempSensor2 = TempSensor("28-00000abcdeff")
presenceSensor = PresenceSensor("GPIO7")

packetSensorData = PacketSensorData()
packetCommandData = PacketCommandData() 

comm = MQTTEMQXCommunication(deviceFunction, deviceId)

comm.begin()
initialTime = time()

while True:
    if time()-initialTime > timeStep:
        packetSensorData.updatePacketSensorData(tempSensor1.getTemp(), tempSensor2.getTemp(), presenceSensor.getPresenceInfo())
        comm.sendPacket(sensorsPacket,packetSensorData.encapsulatePacketSensorData())
        print(f"Mensagem enviada do Rasp para o Centro de Comando")
        initialTime = time()
    if comm.checkMsgIsUpdated():
        print("Mensagem recebida do Centro de Comando para o Raps")
        packetCommandData.decapsulatePacketCommandData(comm.getSensorsDataMsg())
        packetCommandData.printData()
        led.updateLedStatus(packetCommandData.led)
        fan1.updateFanStatus(packetCommandData.fan1)
        fan2.updateFanStatus(packetCommandData.fan2)
        

