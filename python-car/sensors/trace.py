from scape.signal.sensor import SignalSensor
import RPi.GPIO as GPIO


class Trace(SignalSensor):
    def __init__(self):
        super().__init__()
        self.trace_number = [29, 31, 33, 35, 37]
        GPIO.setmode(GPIO.BOARD)
        for index in self.trace_number:
            GPIO.setup(index, GPIO.IN)

    def detective(self, index):
        return GPIO.getmode(self.trace_number[index])
