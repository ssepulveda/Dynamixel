__author__ = 'ssepulveda'

from controlTable import ControlTable
from instructions import Instructions


class BasicInstructions:
    def __init__(self, port):
        self.port = port
        self.reg = ControlTable()
        self.instructions = Instructions()

    def set_led(self, device, enabled):
        self.port.flushOutput()
        self.port.write(self.set_boolean(device, self.reg.LED.address, enabled))
        return self.port.read()

    def set_torque(self, device, enabled):
        self.port.flushOutput()
        self.port.write(self.set_boolean(device, self.reg.TORQUE_ENABLE.address, enabled))
        return self.port.read()

    def set_position(self, device, value):
        [l, h] = self.dec2hex_lh(value)
        self.port.write(self.instructions.write_data_batch(device, self.reg.GOAL_POSITION_L.address, [l, h]))

    def get_position(self, device):
        self.port.write(self.instructions.read_data(device, self.reg.PRESENT_POSITION_L.address, 2))
        return self.port.read()

    def set_speed(self, device, value):
        [l, h] = self.dec2hex_lh(value)
        self.port.write(self.instructions.write_data_batch(device, self.reg.MOVING_SPEED_L.address, [l, h]))

    def get_speed(self, device):
        self.port.write(self.instructions.read_data(device, self.reg.MOVING_SPEED_L.address, 2))
        return self.port.read()

    def set_position_speed(self, device, position, speed):
        [position_l, position_h] = self.dec2hex_lh(position)
        [speed_l, speed_h] = self.dec2hex_lh(speed)
        self.port.write(self.instructions.write_data_batch(device, self.reg.GOAL_POSITION_L.address,
                                                           [position_l, position_h, speed_l, speed_h]))
        return self.port.read()


    def wait_for_device(self, device):
        self.port.write(self.instructions.read_data(device, self.reg.MOVING.address, 1))
        print(self.port.read())

    def set_boolean(self, device, address, enabled):
        if enabled:
            package = self.instructions.write_data(device, address, 1)
        else:
            package = self.instructions.write_data(device, address, 0)
        return package

    @staticmethod
    def dec2hex_lh(value):
        lh = "{0:0{1}X}".format(value, 4)
        return [int(lh[2:4], 16), int(lh[0:2], 16)]