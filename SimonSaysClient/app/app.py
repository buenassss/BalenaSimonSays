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

def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)

    turnOnLedMatrix()
    sys.sleep(1)
    turnOffLedMatrix()

    #send confirmation to server
    print("Send that client has flash correctly", "server/data")
    client.publish("server/data", "P1 Done")

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
    movementDetected = False
    #connecting to server
    print("creating new instance")
    client = mqtt.Client("P1")   #create new instance
    client.on_message=on_message #attach function to callback

    print("connecting to broker")
    client.connect(broker_address) #connect to broker

    client.loop_start() #start the loop
    print("Subscribing to topic", "server/data")
    client.subscribe("server/data")

    while True:
        for event in sense.stick.get_events():
            print("The joystick was {} {}".format(event.action, event.direction))
            if (event.action == "pressed") :
                turnOnLedMatrix()	
            elif (event.action == "released") :
                turnOffLedMatrix()
                print("User move or push raspberry", "server/data")
                client.publish("server/data", "P1 Push")

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1.1 or y > 1.1 or z > 1.1:
            print ("movement is {} {} {}".format(x, y, z))
            turnOnLedMatrix()
            movementDetected = True
        elif movementDetected :
            turnOffLedMatrix()
            movementDetected = False
            print("User move or push raspberry", "server/data")
            client.publish("server/data", "P1 Push")

	        #Send message to server


# Send event to server
