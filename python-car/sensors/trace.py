from scape.core.sensor import Sensor
import RPi.GPIO as GPIO


class Trace(Sensor):
    def __init__(self):
        super().__init__()
        self.trace_number = [29, 31, 33, 35, 37]
        GPIO.setmode(GPIO.BOARD)
        for index in self.trace_number:
            GPIO.setup(index, GPIO.IN)

    def detective(self, index):
        return GPIO.getmode(self.trace_number[index])


class GroupTrace(Trace):
    def __init__(self):
        super().__init__()

    def detective_group(self):
        return self.detective(0), self.detective(1), self.detective(2), self.detective(3), self.detective(4)
