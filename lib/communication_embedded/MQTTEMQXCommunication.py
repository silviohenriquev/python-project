import paho.mqtt.client as mqtt
from lib.communication_embedded.commConfig import version, keepalive, MQTT_HOST, MQTT_PORT, sensorsPacket, commandPacket
import threading

class MQTTEMQXCommunication:
    def __init__(self, deviceFunction, client_id):
        self.deviceFunction = deviceFunction
        self.client_id = client_id
        self.client = None
        self.msgIsUpdated=False
        self.response_callback = None
        self.running = False
    
    def __connect__(self):
        self.client.connect(MQTT_HOST, MQTT_PORT, keepalive)
    
    def __subscribe__(self, topic):
        self.client.subscribe(topic,0)
    
    def __on_message__(self, mosq, obj, msg):
        # This callback will be called for messages that we receive that do not
        # match any patterns defined in topic specific callbacks, i.e. in this case
        # those messages that do not have topics $SYS/broker/messages/# nor
        # $SYS/broker/bytes/#
        #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        self.msgIsUpdated = True 
        self.response_callback = msg.payload

    def begin(self):
        if self.deviceFunction=="publisher":
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.client_id,protocol=version)
            self.__connect__()
            self.__subscribe__(commandPacket)
            self.running = True
            # Inicia uma thread para escutar mensagens
            message_thread = threading.Thread(target=self.listen_for_messages)
            message_thread.start()
        
        if self.deviceFunction=="commandCenter":
            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.client_id,protocol=version)
            self.__connect__()
            self.__subscribe__(sensorsPacket)
            self.running = True
            # Inicia uma thread para escutar mensagens
            message_thread = threading.Thread(target=self.listen_for_messages)
            message_thread.start()
    
    def sendPacket(self, topic, encapsulatedSensorPacket):
        self.client.publish(topic, encapsulatedSensorPacket, qos=0, retain=False)
    
    def listen_for_messages(self):
        self.client.on_message=self.__on_message__
        self.client.loop_forever()
    
    def checkMsgIsUpdated(self):
        return self.msgIsUpdated
    
    def getSensorsDataMsg(self):
        self.msgIsUpdated=False
        return self.response_callback