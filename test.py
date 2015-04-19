__author__ = 'ssepulveda'

from struct import *
import binascii
import serial


HEADER = 0xFFFF
DEVICE_ALL = 0xFE
PING = 0x01
READ_DATA = 0x02
WRITE_DATA = 0x03
REG_WRITE = 0x04
ACTION = 0x05
RESET = 0x06
SYNC_WRITE = 0x83


def read(port):
    try:
        header, device_id, length = unpack('HBB', port.read(4))
        data = unpack(length * 'B', port.read(length))

        if error_type(device_id, data[0]):
            # print(data[0])
            return False
        else:
            if read_crc(data[-1], (device_id + length + sum(data[0:-1]))):
                debug_package([header, data], True)
                return data[0:-1]

        port.flushInput()
    except:
        if port.read(1) == 0:
            port.flushInput()
            return True


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
    instruction = REG_WRITE
    crc = checksum(device_id + length + instruction + param + value)
    return pack('HBBBBBB', HEADER, device_id, length, instruction, param, value, crc)


def action(device_id):
    length = 2
    instruction = ACTION
    crc = checksum(device_id + length + instruction)
    return pack('HBBBB', HEADER, device_id, length, instruction, crc)


def ping(device_id):
    length = 0
    instruction = PING
    crc = checksum(device_id + length + instruction)
    return pack('HBBBB', HEADER, device_id, length, instruction, crc)


def read_data(device_id, address, size):
    length = 4
    instruction = READ_DATA
    crc = checksum(device_id + length + instruction + address + size)
    return pack('HBBBBBB', HEADER, device_id, length, instruction, address, size, crc)


def write_data(device_id, param, value):
    length = 4
    instruction = WRITE_DATA
    crc = checksum(device_id + length + instruction + param + value)
    return pack('HBBBBBB', HEADER, device_id, length, instruction, param, value, crc)


def write_data_batch(device_id, address, values):
    length = 3 + len(values)
    instruction = WRITE_DATA
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
    port.write(set_boolean(device_id, 25, enabled))
    read(port)


def enable_torque(port, device_id, enabled):
    port.flushOutput()
    port.write(set_boolean(device_id, 24, enabled))
    read(port)


def set_boolean(device_id, address, enabled):
    if enabled:
        package = write_data_batch(device_id, address, [1])
    else:
        package = write_data_batch(device_id, address, [0])
    return package


if __name__ == "__main__":
    s = serial.Serial('/dev/ttyUSB0', 1000000, timeout=0.1)

    enable_led(s, DEVICE_ALL, False)
    enable_torque(s, DEVICE_ALL, False)

    s.close()
