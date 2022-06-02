import machine
import network
import ubinascii     # new
import utime
from umqttsimple import MQTTClient

CLIENT_ID = ubinascii.hexlify(machine.unique_id()) # new
#2.4 GHz
SSID     = "duurzaamheidsfabriek"
PASSWORD = "DZHFquest"
TOPIC = "DZHF/ARJAN/TEMPERATURE"        # new
MQTT_BROKER = "192.168.2.128"           # new
SLEEP = 5
station = network.WLAN(network.STA_IF)
station.active(True)

def get_Measurements():          # new
    return "56"

def callback_data(topic, msg):   # new
    print(topic, msg)

def connect():                   # new
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    client.set_callback(callback_data)
    client.connect()
    return client

counter = 1
while True:
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(SSID, PASSWORD)
        utime.sleep(SLEEP)
        
    while station.isconnected():
        print("Connected !")
        print(station.ifconfig())
# ----- new
        try:
            client = connect() 
            countdown = 100
            while countdown > 0:
                data = get_Measurements()
                client.publish(TOPIC, data)
                utime.sleep(SLEEP)
                countdown = countdown - 1
        except OSError as e:
            print(e)
# ------ end new            
        utime.sleep(SLEEP)
