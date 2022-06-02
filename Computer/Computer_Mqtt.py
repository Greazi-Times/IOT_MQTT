import paho.mqtt.client as mqtt
import time
import Computer.computer_constants as constants

# static values
TOPIC = "G7/MOISTURE"
TOPIC2 = "G7/VALVE"

# Check the moisture level and send the data with MQTT to the wemos
def on_message(client, userdata, message):
    topic = message.topic.split('/')
    moisture = float(message.payload.decode("utf-8"))
    if (moisture <= 50):
        valve = 1
    if (moisture > 50):
        valve = 0
    client.publish(TOPIC2, valve)
    print(valve)
    print(f"{topic} : {moisture}")

# Connect to the MQTT client
client = mqtt.Client(constants.mqtt.name)
client.connect(constants.mqtt.host)

# Create a mqtt loop
client.loop_start()

# Subscribe to MQTT client and get the Moisture value
client.subscribe(TOPIC)
client.on_message = on_message

# A loop that allows us to wait a bit before running again
while True:
    # pass # do not use pass... too much CPU consumption
    time.sleep(10)

# Stop the loop
client.loop_stop()