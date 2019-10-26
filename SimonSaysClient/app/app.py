# Server: SimonSaysServer contains the logic to execute simon logic.

from sense_hat import SenseHat
from time import sleep
import socket

sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))

configPath = './conf'
configFile = open(configPath, 'r')
ip = socket.gethostbyname(socket.gethostname())
print ("IP: ", ip)

# Send event to server

