__author__ = 'ssepulveda'

from time import sleep
import sys

from dynamixel.serialCom import SerialCom
from dynamixel.advancedInstructions import AdvancedInstructions
from dynamixel.robot import Robot

if __name__ == "__main__":
    port = SerialCom()
    if port.open_port('/dev/ttyUSB0'):
        print "Can't find serial port"
        sys.exit(0)

    action = AdvancedInstructions(port)
    mark1 = Robot()

    c = 512
    s = 200
    p = 100
    t = .5

    action.reset_all(mark1.all)
    sleep(2)

    # dance
    for i in xrange(0, 9):
        action.move(mark1.shoulder_vertical.left, c+100, s)
        action.move(mark1.shoulder_vertical.right, c+100, s)
        sleep(t)

        action.move(mark1.elbow.left, c-100, s)
        action.move(mark1.elbow.right, c+100, s)
        sleep(t)

        action.move(mark1.shoulder_vertical.left, c-100, s)
        action.move(mark1.shoulder_vertical.right, c-100, s)
        sleep(t)

        action.move(mark1.elbow.left, c+100, s)
        action.move(mark1.elbow.right, c-100, s)
        sleep(t)

    port.close_port()
