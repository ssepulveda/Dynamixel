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

    thigh = 240
    action.move(tobor.thigh.left, c+thigh)
    action.move(tobor.thigh.right, c-thigh)
    action.move(tobor.knee.left, c+300)
    action.move(tobor.knee.right, c-300)
    action.move(tobor.foot_vertical.left, c-100)
    action.move(tobor.foot_vertical.right, c-100)

    sleep(2)

    t = 1
    foot = 50  # angle of the foot
    t2 = 100  # angle of the thight

    """
    @todo implement the waiting function to finish the goal movement
    @todo implement a modification for using angles instead of numbers
    """
    for step in range(0, 4):
        # first step
        sleep(t)
        action.move(tobor.foot_horizontal.right, c+foot, speed=100)
        action.move(tobor.thigh.left, (c+thigh)+t2, speed=50)
        action.move(tobor.foot_vertical.left, c, speed=50)

        sleep(t)
        action.move(tobor.foot_horizontal.right, c, speed=50)
        action.move(tobor.thigh.left, (c+thigh), speed=100)
        action.move(tobor.foot_vertical.left, c-t2, speed=200)

        # second step
        sleep(t)
        action.move(tobor.foot_horizontal.left, c-foot, speed=100)
        sleep(.2) # calibration problem ? takes longer to make the move... or implement wait function
        action.move(tobor.thigh.right, (c-thigh)-t2, speed=50)
        action.move(tobor.foot_vertical.right, c, speed=50)

        sleep(t)
        action.move(tobor.foot_horizontal.left, c, speed=50)
        action.move(tobor.thigh.right, (c-thigh), speed=100)
        action.move(tobor.foot_vertical.right, c-t2, speed=200)

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