import paho.mqtt.client as mqtt 
from random import uniform
import time

import system.logger

CLIENT_NAME = "SmartLab"
MQTT_BROKER = "192.168.1.100"

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)


def measure_temperature():
    return uniform(20.0, 21.0)


while True:
    temperature = measure_temperature()
    client.publish("GROEP7/test", temperature)
    print("Just published to topic TEMPERATURE :", temperature)
    time.sleep(2)
