# Server: SimonSaysServer contains the logic to execute simon logic.

from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt

sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))

# Send event to server

# broker server
broker_address = "10.10.169.177"

def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)

print("creating new instance")
client = mqtt.Client("P1")   #create new instance
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop
print("Subscribing to topic", "server/data")
client.subscribe("server/data")

print("Publishing message to topic", "server/data")
client.publish("server/data", "This is message sent from the servr")

time.sleep(4) # wait
client.loop_stop() #stop the loop

