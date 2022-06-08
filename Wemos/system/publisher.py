from umqttsimple import MQTTClient
import ubinascii
import Wemos.wemos_constants as constants


# Na elke publish de topic en de msg oppakken
def callback_data(topic, msg):
    print(topic, msg)


# Set the connection with the client
def connect(id, host, keepalive):
    client = MQTTClient(id, host, keepalive)
    client.set_callback(callback_data)
    client.connect()
    return client


def push(path, value):
    # Connect to the MQTT system
    client = connect(ubinascii.hexlify(machine.unique_id()), constants.mqtt.host, constants.mqtt.keepalive)

    # Push the data to the system
    client.publish(path, value)


def get(topic):
    # Connect to the MQTT system
    client = connect(ubinascii.hexlify(machine.unique_id()), constants.mqtt.host, constants.mqtt.keepalive)

    return client.subscribe(topic)
