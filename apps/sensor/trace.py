import RPi.GPIO as GPIO


class Trace:
    trace_number = [29, 31, 33, 35, 37]

    def __init__(self):
        GPIO.setmode(GIPO.BOARD)
        for index in self.trace_number:
            GPIO.setup(self.trace_number[index], GPIO.IN)

    def all_0(self):
        for index in self.trace_number:
            if GPIO.getmode(self.trace_number[index]) is not 0:
                return False
        return True

    def all_1(self):
        for index in self.trace_number:
            if GPIO.getmode(self.trace_number[index]) is 0:
                return False
        return True

    def is_0(self, index):
        if GPIO.getmode(self.trace_number[index]) is not 0:
            return False
        return True

    def assume_0(self, assume):
        for (key, value) in assume.items():
            if GPIO.getmode(self.trace_number[key]) is not value:
                return False
        return True
