import platform
import subprocess
import socket


class MQTTEMQXBroker:
    def __init__(self):
        self.cmd = None

    def initializeBroker(self, ip_address):
        self.updateCommand()
        result = subprocess.run(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("Broker Iniciado com Sucesso!")
            print("Endereço IP de acesso:", ip_address)

    def updateCommand(self):
        environment = self.detectEnvironment()
        if environment == "Windows":
            self.cmd = "C:/emqx/bin/emqx start"
        if environment == "Raspbian":
            self.cmd = "sudo systemctl start emqx"

    @staticmethod
    def detectEnvironment():
        os_type = platform.system()
        if os_type == 'Windows':
            return 'Windows'
        else:
            return "Raspbian"

# Uso do código
ip_address = "192.168.1.100"  # Substitua pelo endereço IP desejado
broker = MQTTEMQXBroker()
broker.initializeBroker(ip_address)
