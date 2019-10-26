# Server: SimonSaysServer contains the logic to execute simon logic.

ense_hat import SenseHat
from time import sleep

sense = SenseHat()
event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))

# Send event to server

