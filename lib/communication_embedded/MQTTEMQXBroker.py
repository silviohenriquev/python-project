import platform

import subprocess


class MQTTEMQXBroker:
    def __init__(self):
        self.cmd = None

    def initializeBroker(self):
        self.updateCommand()
        result = subprocess.run(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("Broker Iniciado com Sucesso!")

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
        elif os_type == 'Linux':
            distro = platform.linux_distribution()[0]
            if distro.lower() == 'raspbian':
                return 'Raspbian'
            else:
                return 'Linux (Other)'
        else:
            return 'Unknown'