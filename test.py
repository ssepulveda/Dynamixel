__author__ = 'ssepulveda'

from struct import *
import binascii
import serial
from time import sleep

from dynamixel.controlTable import *


def read(port):
    try:
        header, device_id, length = unpack('HBB', port.read(4))
        data = unpack(length * 'B', port.read(length))

        if error_type(device_id, data[0]):
            return False
        else:
            if read_crc(data[-1], (device_id + length + sum(data[0:-1]))):
                return data[1:-1]

        port.flushInput()
    except:
        print(port.read(100))


def error_type(device_id, value):
    if value == 0:
        return False
    else:
        txt = "Error in Device " + str(device_id) + ": "
        if value == 64:
            txt += "Instruction "
        if value == 32:
            txt += "Overload "
        if value == 16:
            txt += "Checksum "
        if value == 8:
            txt += "Overheating "
        if value == 4:
            txt += "Angle Limit"
        if value == 2:
            txt += "Input Voltage "
        print(txt)
        return True


def read_crc(crc_in, data):
    crc = checksum(data)
    if crc == crc_in:
        return True
    else:
        return False


def checksum(value):
    return (~value) & 0xFF


def reg_write(device_id, param, value):
    length = 4
    instruction = instruct.REG_WRITE
    crc = checksum(device_id + length + instruction + param + value)
    return pack('HBBBBBB', instruct.HEADER, device_id, length, instruction, param, value, crc)


def action(device_id):
    length = 2
    instruction = instruct.ACTION
    crc = checksum(device_id + length + instruction)
    return pack('HBBBB', instruct.HEADER, device_id, length, instruction, crc)


def ping(device_id):
    length = 0
    instruction = instruct.PING
    crc = checksum(device_id + length + instruction)
    return pack('HBBBB', instruct.HEADER, device_id, length, instruction, crc)


def read_data(device_id, address, size):
    length = 4
    instruction = instruct.READ_DATA
    crc = checksum(device_id + length + instruction + address + size)
    return pack('HBBBBBB', instruct.HEADER, device_id, length, instruction, address, size, crc)


def write_data(device_id, param, value):
    length = 4
    instruction = 3
    crc = checksum(device_id + length + instruction + param + value)
    return pack('HBBBBBB', 0xFFFF, device_id, length, instruction, param, value, crc)


def write_data_batch(device_id, address, values):
    length = 3 + len(values)
    instruction = instruct.WRITE_DATA
    crc = checksum(device_id + length + instruction + address + sum(values))
    data = [device_id, length, instruction, address] + values
    return "".join(map(chr, [0xFF, 0xFF] + data + [crc]))


def debug_package(package, is_input=False):
    txt = ""
    if is_input:
        txt += "<-"
    else:
        txt += "->"
    txt += "[Dynamixel]: " + binascii.hexlify(package)
    print(txt)
    return package


def enable_led(port, device_id, enabled):
    port.flushOutput()
    port.write(set_boolean(device_id, reg.LED.address, enabled))
    return read(port)


def enable_torque(port, device_id, enabled):
    port.flushOutput()
    port.write(set_boolean(device_id, reg.TORQUE_ENABLE.address, enabled))
    return read(port)


def set_boolean(device_id, address, enabled):
    if enabled:
        package = write_data(device_id, address, 1)
    else:
        package = write_data(device_id, address, 0)
    return package


def dec2hex_lh(value):
    lh = "{0:0{1}X}".format(value, 4)
    return int(lh[2:4], 16), int(lh[0:2], 16)


def goal_position(device_id, value):
    [l, h] = dec2hex_lh(value)
    s.write(write_data_batch(device_id, reg.GOAL_POSITION_L.address, [l, h]))


def moving_speed(device_id, value):
    [l, h] = dec2hex_lh(value)
    s.write(write_data_batch(device_id, reg.MOVING_SPEED_L.address, [l, h]))


def goto(serial, device_id, goal, speed=1023):
    [goal_l, goal_h] = dec2hex_lh(goal)
    [speed_l, speed_h] = dec2hex_lh(speed)
    serial.write(write_data_batch(device_id, reg.GOAL_POSITION_L.address, [goal_l, goal_h, speed_l, speed_h]))
    check = read(serial)
    print(check)


if __name__ == "__main__":
    s = serial.Serial('/dev/ttyUSB0', 1000000, timeout=0.1)

    instruct = Instruction()
    reg = ControlTable()

    goto(s, 1, 0)
    goto(s, 2, 0)
    print(read(s))

    s.close()
