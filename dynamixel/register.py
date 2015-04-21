__author__ = 'ssepulveda'


class Register():

    def __init__(self, address, mode='r', eeprom=False):
        self.address = address
        self.mode = mode
        self.eeprom = eeprom