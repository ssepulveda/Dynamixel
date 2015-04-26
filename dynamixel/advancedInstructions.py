__author__ = 'ssepulveda'

from basicInstructions import BasicInstructions


class AdvancedInstructions:
    def __init__(self, port):
        self.port = port
        self.actions = BasicInstructions(port)
        self.center = 512

    def move(self, device, position, speed=1023):
        response = self.actions.set_position_speed(device, position, speed)
        return response

    def reset_all(self, devices, speed=200):
        for device in devices:
            self.move(device, self.center, speed)