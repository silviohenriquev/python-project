import paho.mqtt.client as mqtt

version = mqtt.MQTTv5
MQTT_HOST = "localhost"
MQTT_PORT = 1883
keepalive = 60

sensorsPacket = "sensorPacket/"
commandPacket = "commandPacket/"