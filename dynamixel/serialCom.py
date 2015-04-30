__author__ = 'ssepulveda'

from struct import unpack
from controlTable import Validate
import binascii
import serial


class SerialCom():
    def __init__(self):
        self.port = serial.Serial()
        self.header = None
        self.device = None
        self.length = None
        self.validate = Validate()

    def open_port(self, port='/dev/ttyUSB0', baudrate=1000000, timeout=0.1):
        self.port.port = port
        self.port.baudrate = baudrate
        self.port.timeout = timeout
        self.port.stopbits = serial.STOPBITS_ONE
        self.port.bytesize = serial.EIGHTBITS

        if self.port.isOpen():
            return False
        else:
            try:
                self.port.open()
                # self.port.flushOutput()
                # self.port.flushInput()
                return True
            except:
                raise
                return False

    def close_port(self):
        try:
            self.port.close()
        except:
            raise
        finally:
            return not self.port.isOpen()

    def read(self):
        try:
            package = self.port.read(4)
            print("< " + binascii.hexlify(package))
            header, self.device, length = unpack('HBB', package)
            data = unpack(length * 'B', self.port.read(length))

            if not self.validate.is_error(data[0]):
                if self.validate.check(data[-1], (self.device + length + sum(data[0:-1]))):
                    return data[1:-1]
                else:
                    return False
            else:
                return self.validate.is_error(data[0])
        except:
            raise
        finally:
            self.port.flushInput()

    def write(self, package):
        self.port.write(package)
        print("> " + binascii.hexlify(package))
        self.port.flushOutput()
