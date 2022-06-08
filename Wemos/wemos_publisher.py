import wemos_constants
import system.publisher as mqtt
import network
import utime
import wemos_constants as constants
from machine import ADC, Pin


# Valve components
p2 = Pin(2, Pin.OUT)

# Moisture components
soil = ADC(0)
min_moisture = 0
max_moisture = 65535

# The connection to the network
station = network.WLAN(network.STA_IF)
station.active(True)

# Returns the values of the HW-390 Moisture Sensor
def get_moisture():
    return ((max_moisture-soil.read_u16())*100/(max_moisture-min_moisture))


# Returns the value of the valve
def get_valve():
    return p2


# The main system that runs in a loop
counter = 1
while True:
    # Connect to the network
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(constants.network.host, constants.network.password)
        utime.sleep(5)

    # Check if system is connected to the network
    if (station.isconnected()):
        while True:
            # Send success message
            print("Connected !")
            print(station.ifconfig())

            # Try to connect to the MQTT system.
            try:
                # Static getters
                moisture = get_moisture()

                # Send all data to MQTT server
                mqtt.push('G7/MOISTURE', moisture)

                # Get valve that return a 0 or a 1
                valve = mqtt.get(constants.mqtt.topic)

                # A for loop that checks how many valves are connected to the system
                for x in range(constants.system.valves):
                    x += 2
                    pin = Pin(x, Pin.OUT)
                    pin(valve)

                # Check print for console to see moisture and valve value's
                print("Published Moisture: " + moisture + " Valve: " + valve)

                # Wait a little before continuing
                utime.sleep(5)

            # Send an exception
            except OSError as e:
                print(e)

            # Wait a little before continuing
            utime.sleep(5)

# A disabled print for checking the moisture system
# print("moisture: " + "%.2f" % get_moisture() + "% (adc: " + str(soil.read_u16()) + ")")
