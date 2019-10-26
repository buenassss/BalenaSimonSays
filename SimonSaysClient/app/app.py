# Client: SimonSaysClient contains the logic to execute simon logic.

from sense_hat import SenseHat
from time import sleep
import socket, sys

sense = SenseHat()

def turnOffLedMatrix():
	O = [0, 0, 0]  # black

	screen = [
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O
	]

	sense.set_pixels(screen)

def turnOnLedMatrix():
	
	O = [255, 255, 255]  # White

	screen = [
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O,
	O, O, O, O, O, O, O, O
	]

	sense.set_pixels(screen)

ip = socket.gethostbyname(socket.gethostname())
print("Hostname: ", socket.gethostname())
print ("IP: ", ip)

configPath = './conf'
configFile = open(configPath, 'r')
hostname = configFile.readline()

if hostname == socket.gethostname():
    print("SERVER -> exit")
    sys.exit(0)
else:
    print("CLIENT")

    #wait message from server
    
    while True:
        for event in sense.stick.get_events():
            print("The joystick was {} {}".format(event.action, event.direction))
            turnOnLedMatrix()	
            time.sleep(1)
            turnOffLedMatrix()

	        #Send message to server


# Send event to server
