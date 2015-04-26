__author__ = 'ssepulveda'

from controlTable import Validate
from struct import pack


class Instructions:
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

        self.validate = Validate()

    def reg_write(self, device, param, value):
        length = 4
        instruction = self.REG_WRITE
        crc = self.validate.checksum(device + length + instruction + param + value)
        return pack('HBBBBBB', self.HEADER, device, length, instruction, param, value, crc)

    def action(self, device):
        length = 2
        instruction = self.ACTION
        crc = self.validate.checksum(device + length + instruction)
        return pack('HBBBB', self.HEADER, device, length, instruction, crc)
    
    def ping(self, device):
        length = 0
        instruction = self.PING
        crc = self.validate.checksum(device + length + instruction)
        return pack('HBBBB', self.HEADER, device, length, instruction, crc)

    def read_data(self, device, address, size):
        length = 4
        instruction = self.READ_DATA
        crc = self.validate.checksum(device + length + instruction + address + size)
        return pack('HBBBBBB', self.HEADER, device, length, instruction, address, size, crc)
    
    def write_data(self, device, param, value):
        length = 4
        instruction = 3
        crc = self.validate.checksum(device + length + instruction + param + value)
        return pack('HBBBBBB', 0xFFFF, device, length, instruction, param, value, crc)

    def write_data_batch(self, device, address, values):
        length = 3 + len(values)
        instruction = self.WRITE_DATA
        crc = self.validate.checksum(device + length + instruction + address + sum(values))
        data = [device, length, instruction, address] + values
        return "".join(map(chr, [0xFF, 0xFF] + data + [crc]))

