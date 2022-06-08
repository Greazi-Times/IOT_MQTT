import paho.mqtt.client as mqtt
import time
import computer_constants as constants
import Logger as logger

# static values
TOPIC = "G7/MOISTURE"
TOPIC2 = "G7/VALVE"

# Check if the logg file exists
logger.exists(constants.file.logger)

# Check the moisture level and send the data with MQTT to the wemos
def on_message(client, userdata, message):
    # Split the topic
    topic = message.topic.split('/')
    # Decode the moisture value
    moisture = float(message.payload.decode("utf-8"))
    # Check the moisture values
    if (moisture <= 50):
        valve = 1
    if (moisture > 50):
        valve = 0

    # Send the valve value to the mqtt system
    client.publish(TOPIC2, valve)

    # Create a data object of the values
    data = [str(moisture), str(valve)]
    # Save the data object in the logger
    #logger.add(data)

    # Console print system that allow you to check the values
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