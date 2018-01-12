import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 7
sensor_pin = 16
j = 3
i = 5.2

while RPL.digitalRead(sensor_pin) == 1:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    if RPL.digitalRead(sensor_pin) != 1:
        break


while RPL.digitalRead(sensor_pin) == 0:
    move = time.time()
    while time.time() < (move + i):
        RPL.servoWrite(motorR, 1480)
        RPL.servoWrite(motorL, 1570)
    while time.time() > (move + i):
        RPL.servoWrite(motorR, 1000)
        RPL.servoWrite(motorL, 2000)