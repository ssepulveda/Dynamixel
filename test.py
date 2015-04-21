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


def dec2hex_LH(value):
    print unpack('BB', value)


if __name__ == "__main__":
    s = serial.Serial('/dev/ttyUSB0', 1000000, timeout=0.1)

    instruct = Instruction()
    reg = ControlTable()

    s.write(read_data(1, 0, 49))
    print(read(s))

    s.write(read_data(2, 0, 49))
    print(read(s))

    device = instruct.BROADCAST
    enable_led(s, device, True)
    enable_torque(s, device, True)

    device = 6


    s.write(write_data_batch(device, 0x1E, [0x00, 0x03, 0x00, 0x02]))
    print(read(s))
    s.write(write_data_batch(2, 0x1E, [0xFF, 0x00, 0x00, 0x02]))
    print(read(s))

    sleep(1)

    s.write(write_data_batch(device, 0x1E, [0x20, 0x03, 0x00, 0x02]))
    print(read(s))

    sleep(1)

    s.write(write_data_batch(device, 0x1E, [0x00, 0x03, 0x00, 0x02]))
    print(read(s))

    sleep(1)

    s.write(write_data_batch(device, 0x1E, [0x00, 0x02, 0x00, 0x02]))
    print(read(s))
    s.write(write_data_batch(2, 0x1E, [0x00, 0x02, 0x00, 0x02]))
    print(read(s))

    device = instruct.BROADCAST
    enable_led(s, device, False)
    enable_torque(s, device, False)

    device = 2

    s.close()
