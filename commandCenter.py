import tkinter as tk
from lib.sensors import *
from lib.communication_embedded.MQTTEMQXCommunication import MQTTEMQXCommunication
from lib.communication_embedded.MQTTEMQXBroker import MQTTEMQXBroker
from lib.communication_embedded.commTypes import *
from lib.communication_embedded.commConfig import *
from lib.tkInter import InterfaceTemperaturas


deviceFunction = "commandCenter"
deviceId = "commandCenter"

packetSensorData = PacketSensorData()
packetCommandData = PacketCommandData()

comm = MQTTEMQXCommunication(deviceFunction, deviceId)
broker = MQTTEMQXBroker()

broker.initializeBroker()
comm.begin()

print("Iniciando o Centro de Comandos")

def update_interface():
    if comm.checkMsgIsUpdated():
        packetSensorData.decapsulatePacketSensorData(comm.getSensorsDataMsg())
        app.updateSensorsData(packetSensorData.temp1, packetSensorData.temp2, packetSensorData.presenceSensor)
        print("Mensagem Recebida do Raps para o Centro de Comando")
    
    if app.checkCommandIsUpdated():
        packetCommandData.updatePacketCommandData(* app.getSwitchInfo())
        comm.sendPacket(commandPacket, packetCommandData.encapsulatePacketCommandData())
        print("Mensagem Enviada do Centro de Comando para o Rasp")
    root.after(1000, update_interface)  # Agendar próxima atualização

# Criar a janela principal
root = tk.Tk()
app = InterfaceTemperaturas(root)
root.title("Centro de Comandos")

# Iniciar atualização da interface
update_interface()

root.mainloop()
