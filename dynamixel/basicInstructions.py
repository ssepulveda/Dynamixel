__author__ = 'ssepulveda'

from controlTable import ControlTable
from instructions import Instructions


class BasicInstructions:
    def __init__(self, port):
        self.port = port
        self.reg = ControlTable()
        self.instructions = Instructions()

    # EEPROM Area Instructions

    def get_model_number(self, device):
        return self.read_register(device, self.reg.MODEL_NUMBER_L)

    def get_firmware_version(self, device):
        return self.read_register(device, self.reg.FIRMWARE_VERSION)

    def get_id(self, device):
        return self.read_register(device, self.reg.ID)

    def set_id(self, device, value):
        return self.write_register(device, self.reg.ID, value)

    def get_baudrate(self, device):
        return self.read_register(device, self.reg.BAUD_RATE)

    def set_baudrate(self, device, value):
        return self.write_register(device, self.reg.BAUD_RATE, value)

    def get_return_delay(self, device):
        return self.read_register(device, self.reg.RETURN_DELAY)

    def set_return_delay(self, device, value):
        return self.write_register(device, self.reg.RETURN_DELAY, value)

    def get_cw_angle_limit(self, device):
        return self.read_register(device, self.reg.CW_ANGLE_LIMIT_L)

    def set_cw_angle_limit(self, device, value):
        return self.write_register(device, self.reg.CW_ANGLE_LIMIT_L, value)

    def get_ccw_angle_limit(self, device):
        return self.read_register(device, self.reg.CCW_ANGLE_LIMIT_L)

    def set_ccw_angle_limit(self, device, value):
        return self.write_register(device, self.reg.CCW_ANGLE_LIMIT_L, value)

    def get_highest_limit_temperature(self, device):
        return self.read_register(device, self.reg.HIGHEST_LIMIT_TEMPERATURE)

    def set_highest_limit_temperature(self, device, value):
        return self.write_register(device, self.reg.HIGHEST_LIMIT_TEMPERATURE, value)

    def get_lowest_limit_voltage(self, device):
        return self.read_register(device, self.reg.LOWEST_LIMIT_VOLTAGE)

    def set_lowest_limit_voltage(self, device, value):
        return self.write_register(device, self.reg.LOWEST_LIMIT_VOLTAGE, value)

    def get_highest_limit_voltage(self, device):
        return self.read_register(device, self.reg.HIGHEST_LIMIT_VOLTAGE)

    def set_highest_limit_voltage(self, device, value):
        return self.write_register(device, self.reg.HIGHEST_LIMIT_VOLTAGE, value)

    def get_max_torque(self, device):
        return self.read_register(device, self.reg.MAX_TORQUE_L)

    def set_max_torque(self, device, value):
        return self.write_register(device, self.reg.MAX_TORQUE_L, value)

    def get_status_return_level(self, device):
        return self.read_register(device, self.reg.STATUS_RETURN_LEVEL)

    def set_status_return_level(self, device, value):
        return self.write_register(device, self.reg.STATUS_RETURN_LEVEL, value)

    def get_alarm_led(self, device):
        return self.read_register(device, self.reg.ALARM_LED)

    def set_alarm_led(self, device, value):
        return self.write_register(device, self.reg.ALARM_LED, value)

    def get_alarm_shutdown(self, device):
        return self.read_register(device, self.reg.ALARM_SHUTDOWN)

    def set_alarm_shutdown(self, device, value):
        return self.write_register(device, self.reg.ALARM_SHUTDOWN, value)

    def get_down_calibration(self, device):
        return self.read_register(device, self.reg.DOWN_CALIBRATION_L)

    def get_up_calibration(self, device):
        return self.read_register(device, self.reg.UP_CALIBRATION_L)

    # RAM Area Instruction

    def get_torque(self, device):
        return self.read_register(device, self.reg.TORQUE_ENABLE)

    def set_torque(self, device, enabled):
        return self.set_boolean(device, self.reg.TORQUE_ENABLE.address, enabled)

    def get_led(self, device):
        return self.read_register(device, self.reg.LED)

    def set_led(self, device, enabled):
        return self.set_boolean(device, self.reg.LED.address, enabled)

    def get_cw_compliance_margin(self, device):
        return self.read_register(device, self.reg.CW_COMPLIANCE_MARGIN)

    def set_cw_compliance_margin(self, device, value):
        return self.write_register(device, self.reg.CW_COMPLIANCE_MARGIN, value)

    def get_ccw_compliance_margin(self, device):
        return self.read_register(device, self.reg.CCW_COMPLIANCE_MARGIN)

    def set_ccw_compliance_margin(self, device, value):
        return self.write_register(device, self.reg.CCW_COMPLIANCE_MARGIN, value)

    def get_cw_compliance_slope(self, device):
        return self.read_register(device, self.reg.CW_COMPLIANCE_SLOPE)

    def set_cw_compliance_slope(self, device, value):
        return self.write_register(device, self.reg.CW_COMPLIANCE_SLOPE, value)

    def get_ccw_compliance_slope(self, device):
        return self.read_register(device, self.reg.CCW_COMPLIANCE_SLOPE)

    def set_ccw_compliance_slope(self, device, value):
        return self.write_register(device, self.reg.CCW_COMPLIANCE_SLOPE, value)

    def get_goal_position(self, device):
        return self.read_register(device, self.reg.GOAL_POSITION_L)

    def set_goal_position(self, device, value):
        return self.write_register(device, self.reg.GOAL_POSITION_L, value)

    def get_speed(self, device):
        return self.read_register(device, self.reg.MOVING_SPEED_L)

    def set_speed(self, device, value):
        return self.write_register(device, self.reg.MOVING_SPEED_L, value)

    def get_torque_limit(self, device):
        return self.read_register(device, self.reg.TORQUE_LIMIT_L)

    def set_torque_limit(self, device, value):
        return self.write_register(device, self.reg.TORQUE_LIMIT_L, value)

    def get_present_position(self, device):
        return self.read_register(device, self.reg.PRESENT_POSITION_L)

    def get_present_speed(self, device):
        return self.read_register(device, self.reg.PRESENT_SPEED_L)

    def get_present_load(self, device):
        return self.read_register(device, self.reg.PRESENT_LOAD_L)

    def get_present_voltage(self, device):
        return self.read_register(device, self.reg.PRESENT_VOLTAGE)

    def get_present_temperature(self, device):
        return self.read_register(device, self.reg.PRESENT_TEMPERATURE)

    def get_registered_instruction(self, device):
        return self.read_register(device, self.reg.REGISTERED_INSTRUCTION)

    def set_registered_instruction(self, device, value):
        return self.write_register(device, self.reg.REGISTERED_INSTRUCTION, value)

    def get_moving(self, device):
        return self.read_register(device, self.reg.MOVING)

    def get_lock(self, device):
        return self.read_register(device, self.reg.LOCK)

    def set_lock(self, device, value):
        return self.write_register(device, self.reg.LOCK, value)

    def get_punch(self, device):
        return self.read_register(device, self.reg.PUNCH_L)

    def set_punch(self, device, value):
        return self.write_register(device, self.reg.PUNCH_L, value)

    # helpers

    def read_register(self, device, register):
        """

        :type device: int the motor device number (ID)
        :type register: register object containing address, and size
        """
        self.port.write(self.instructions.read_data(device, register.address, register.size))
        return self.port.read()

    def write_register(self, device, register, value):
        if register.mode == 'rw':
            if register.size == 2:
                [l, h] = self.dec2hex_lh(value)
                self.port.write(self.instructions.write_data_batch(device, register.address, [l, h]))
                return self.port.read()
            elif register.size == 1:
                self.port.write(self.instructions.write_data(device, register.address, value))
                return self.port.read()
            else:
                return False
        else:
            return False

    def set_boolean(self, device, register, enabled):
        if enabled:
            package = self.write_register(device, register, 1)
        else:
            package = self.write_register(device, register, 0)
        return package

    @staticmethod
    def dec2hex_lh(value):
        lh = "{0:0{1}X}".format(value, 4)
        return [int(lh[2:4], 16), int(lh[0:2], 16)]

    # batch sequences

    def set_position_speed(self, device, position, speed):
        [position_l, position_h] = self.dec2hex_lh(position)
        [speed_l, speed_h] = self.dec2hex_lh(speed)
        self.port.write(self.instructions.write_data_batch(device, self.reg.GOAL_POSITION_L.address,
                                                           [position_l, position_h, speed_l, speed_h]))
        return self.port.read()
