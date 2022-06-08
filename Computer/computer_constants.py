# ----------------------------------------------------------------------------------#
#        Constants is a file that contains all the values used over
#       the whole project. There for making it easy to change values
# ----------------------------------------------------------------------------------#

# All file related values
class file:
    logger = "logs/systemLogs.csv"

# All MQTT related values
class mqtt:
    host = "192.168.1.99"
    port = 1883
    keepalive = 60
    name = "computer"
    topic = [("DZHF/G7/TEMPERATURE/+", 0), ("DZHF/G7/VALVE/+", 0)]
