import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    temp_value = message.payload
    temp_string = str(temp_value)
    
    print("Message received: "  + temp_string)
    with open(r'C:\Users\Gebruiker\OneDrive\Bureaublad\Bewatering Systeem\Python Code Aanpassen\test.txt','a+') as f:
         f.write("Message received: "  + temp_string + "\n")

Connected = False   #global variable for the state of the connection

broker_address= "192.168.1.99"  #Broker address
port = 1883                      #Broker port
user = "MQTT_WIFI"      #Connection username
password = "KambergArjan"            #Connection password

client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
client.connect(broker_address,port,60) #connect
client.subscribe("Groep_9/Moisture_Soil") #subscribe
client.loop_forever() #then keep listening forever