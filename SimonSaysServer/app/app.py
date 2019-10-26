# Server: SimonSaysServer contains the logic to execute simon logic.

from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt
#import socket, sys

#ip = socket.gethostbyname(socket.gethostname())
#print("Hostname: ", socket.gethostname())
#print ("IP: ", ip)

#sense = SenseHat()
#event = sense.stick.wait_for_event()
#print("The joystick was {} {}".format(event.action, event.direction))

#configPath = './conf'
#configFile = open(configPath, 'r')
#hostname = configFile.readline()

'''
print ("Socket hostname: ", socket.gethostname())
print ("Config hostname: ", hostname)
if hostname == socket.gethostname():
    print("SERVER")
else:
    print("CLIENT -> exit")
    sys.exit(0)
'''

# broker server
broker_address = "10.10.169.177"
broker_port = 1883

def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)

print("creating new instance")
client = mqtt.Client("P1")   #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address, port=broker_port) #connect to broker

client.loop_start() #start the loop
print("Subscribing to topic", "server/data")
client.subscribe("server/data")

print("Publishing message to topic", "server/data")
client.publish("server/data", "This is message sent from the servr")

time.sleep(4) # wait
client.loop_stop() #stop the loop

# Send event to server
