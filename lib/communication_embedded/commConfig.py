import paho.mqtt.client as mqtt

version = mqtt.MQTTv5
MQTT_HOST = "192.168.56.1"
MQTT_PORT = 1883
keepalive = 60

sensorsPacket = "sensorPacket/"
commandPacket = "commandPacket/"