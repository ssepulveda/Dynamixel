__author__ = 'ssepulveda'


from register import *


class ControlTable:
    def __init__(self):
        # EEPROM Area
        self.MODEL_NUMBER_L = Register(0, eeprom=True)
        self.MODEL_NUMBER_H = Register(1, eeprom=True)
        self.FIRMWARE_VERSION = Register(2, eeprom=True)
        self.ID = Register(3, mode='rw', eeprom=True)
        self.BAUD_RATE = Register(4, mode='rw', eeprom=True)
        self.RETURN_DELAY = Register(5, mode='rw', eeprom=True)
        self.CW_ANGLE_LIMIT_L = Register(6, mode='rw', eeprom=True)
        self.CW_ANGLE_LIMIT_H = Register(7, mode='rw', eeprom=True)
        self.CCW_ANGLE_LIMIT_L = Register(8, mode='rw', eeprom=True)
        self.CCW_ANGLE_LIMIT_H = Register(9, mode='rw', eeprom=True)
        self.HIGHEST_LIMIT_TEMPERATURE = Register(11, mode='rw', eeprom=True)
        self.LOWEST_LIMIT_VOLTAGE = Register(12, mode='rw', eeprom=True)
        self.HIGHEST_LIMIT_VOLTAGE = Register(13, mode='rw', eeprom=True)
        self.MAX_TORQUE_L = Register(14, mode='rw', eeprom=True)
        self.MAX_TORQUE_H = Register(15, mode='rw', eeprom=True)
        self.STATUS_RETURN_LEVEL = Register(16, mode='rw', eeprom=True)
        self.ALARM_LED = Register(17, mode='rw', eeprom=True)
        self.ALARM_SHUTDOWN = Register(18, mode='rw', eeprom=True)
        self.DOWN_CALIBRATION_L = Register(20, eeprom=True)
        self.DOWN_CALIBRATION_H = Register(21, eeprom=True)
        self.UP_CALIBRATION_L = Register(22, eeprom=True)
        self.UP_CALIBRATION_H = Register(23, eeprom=True)

        # RAM Area
        self.TORQUE_ENABLE = Register(24, mode='rw')
        self.LED = Register(25, mode='rw')
        self.CW_COMPLIANCE_MARGIN = Register(26, mode='rw')
        self.CCW_COMPLIANCE_MARGIN = Register(27, mode='rw')
        self.CW_COMPLIANCE_SLOPE = Register(28, mode='rw')
        self.CCW_COMPLIANCE_SLOPE = Register(29, mode='rw')
        self.GOAL_POSITION_L = Register(30, mode='rw')
        self.GOAL_POSITION_H = Register(31, mode='rw')
        self.MOVING_SPEED_L = Register(32, mode='rw')
        self.MOVING_SPEED_H = Register(33, mode='rw')
        self.TORQUE_LIMIT_L = Register(34, mode='rw')
        self.TORQUE_LIMIT_H = Register(35, mode='rw')
        self.PRESENT_POSITION_L = Register(36)
        self.PRESENT_POSITION_H = Register(37)
        self.PRESENT_SPEED_L = Register(38)
        self.PRESENT_SPEED_H = Register(39)
        self.PRESENT_LOAD_L = Register(40)
        self.PRESENT_LOAD_H = Register(41)
        self.PRESENT_VOLTAGE = Register(42)
        self.PRESENT_TEMPERATURE = Register(43)
        self.REGISTERED_INSTRUCTION = Register(44, mode='rw')
        self.MOVING = Register(46)
        self.LOCK = Register(47, mode='rw')
        self.PUNCH_L = Register(48, mode='rw')
        self.PUNCH_H = Register(49, mode='rw')


class Instruction:
    def __init__(self):
        self.HEADER = 0xFFFF
        self.BROADCAST = 0xFE
        self.PING = 0x01
        self.READ_DATA = 0x02
        self.WRITE_DATA = 0x03
        self.REG_WRITE = 0x04
        self.ACTION = 0x05
        self.RESET = 0x06
        self.SYNC_WRITE = 0x83


class Validate:
    def __init__(self):
        self.INSTRUCTION = 64
        self.OVERLOAD = 32
        self.CHECKSUM = 16
        self.OVERHEATING = 8
        self.ANGLE_LIMIT = 4
        self.INPUT_VOLTAGE = 2
        self.NO_ERROR = 0

    def is_error(self, error):
        if error == self.NO_ERROR:
            return False
        else:
            return [True, error]

    def check(self, crc_in, data):
        crc = self.checksum(data)
        if crc == crc_in:
            return True
        else:
            return False

    @staticmethod
    def checksum(value):
        return (~value) & 0xFF
