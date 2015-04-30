__author__ = 'ssepulveda'

from time import sleep
import sys

from dynamixel.serialCom import SerialCom
from dynamixel.advancedInstructions import AdvancedInstructions
from dynamixel.robot import Robot

if __name__ == "__main__":
    port = SerialCom()
    if not port.open_port(port='/dev/ttyUSB1'):
        print "Can't find serial port"
        sys.exit(0)

    action = AdvancedInstructions(port)
    tobor = Robot()

    c = 512
    s = 200
    p = 100
    t = .5

    # action.reset_all(tobor.all)
    # sleep(2)

    # reset lower extremities
    action.move(tobor.knee.left, c)
    action.move(tobor.knee.right, c)
    action.move(tobor.hip.left, c)
    action.move(tobor.hip.right, c)
    action.move(tobor.thigh.left, c)
    action.move(tobor.thigh.right, c)
    action.move(tobor.foot_horizontal.left, c)
    action.move(tobor.foot_horizontal.right, c)
    action.move(tobor.foot_vertical.left, c)
    action.move(tobor.foot_vertical.right, c)

    # initial postion to walk
    p = 300
    action.move(tobor.thigh.left, c+200)
    action.move(tobor.thigh.right, c-200)
    action.move(tobor.knee.left, c+p)
    action.move(tobor.knee.right, c-p)
    action.move(tobor.foot_vertical.left, c-100)
    action.move(tobor.foot_vertical.right, c-100)



    # dance
    """
    for i in xrange(0, 9):
        action.move(tobor.shoulder_vertical.left, c+100, s)
        action.move(tobor.shoulder_vertical.right, c+100, s)
        sleep(t)

        action.move(tobor.elbow.left, c-100, s)
        action.move(tobor.elbow.right, c+100, s)
        sleep(t)

        action.move(tobor.shoulder_vertical.left, c-100, s)
        action.move(tobor.shoulder_vertical.right, c-100, s)
        sleep(t)

        action.move(tobor.elbow.left, c+100, s)
        action.move(tobor.elbow.right, c-100, s)
        sleep(t)
    """

    port.close_port()
