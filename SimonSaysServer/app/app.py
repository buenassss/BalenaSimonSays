# Server: SimonSaysServer contains the logic to execute simon logic.

from sense_hat import SenseHat
from time import sleep
import socket, sys

ip = socket.gethostbyname(socket.gethostname())
print("Hostname: ", socket.gethostname())
print ("IP: ", ip)

sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))

configPath = './conf'
configFile = open(configPath, 'r')
hostname = configFile.readline()

if hostname == socket.gethostname():
    print("SERVER")
else:
    print("CLIENT -> exit")
    sys.exit(0)


# Send event to server
