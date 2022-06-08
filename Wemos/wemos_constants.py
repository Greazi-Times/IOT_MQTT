#----------------------------------------------------------------------------------#
#        Constants is a file that contains all the values used over
#       the whole project. There for making it easy to change values
#----------------------------------------------------------------------------------#

# All MQTT related values
class mqtt:
    host = "192.168.2.128"
    port = 1883
    keepalive = 60
    valve_topic = "G7/VALVE"


class system:
    valves = 1

# All Network related values
class network:
    host = "MQTT_WIFI"
    password = "DZHFguest"
