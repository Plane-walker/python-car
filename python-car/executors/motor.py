from scape.core.executor import Executor
import RPi.GPIO as GPIO


class Motor(Executor):
    def __init__(self):
        super().__init__()
        self.config = {'al': [38, 40, 33],
                       'ar': [36, 32, 12],
                       'bl': [13, 15, 33],
                       'br': [11, 7, 12],
                       'speed_check': [18, 14, 33, 35]}
        GPIO.setmode(GPIO.BOARD)
        for index in self.config:
            GPIO.setup(self.config[index][0], GPIO.OUT)
            GPIO.setup(self.config[index][1], GPIO.OUT)

    def go_ahead(self):
        for index in self.config:
            GPIO.output(self.config[index][0], 1)
            GPIO.output(self.config[index][1], 0)

    def go_back(self):
        for index in self.config:
            GPIO.output(self.config[index][0], 0)
            GPIO.output(self.config[index][1], 1)

    def go_left(self):
        GPIO.output(self.config['al'][0], 1)
        GPIO.output(self.config['al'][1], 0)
        GPIO.output(self.config['ar'][0], 0)
        GPIO.output(self.config['ar'][1], 1)
        GPIO.output(self.config['bl'][0], 0)
        GPIO.output(self.config['bl'][1], 1)
        GPIO.output(self.config['br'][0], 1)
        GPIO.output(self.config['br'][1], 0)

    def go_right(self):
        GPIO.output(self.config['al'][0], 0)
        GPIO.output(self.config['al'][1], 1)
        GPIO.output(self.config['ar'][0], 1)
        GPIO.output(self.config['ar'][1], 0)
        GPIO.output(self.config['bl'][0], 1)
        GPIO.output(self.config['bl'][1], 0)
        GPIO.output(self.config['br'][0], 0)
        GPIO.output(self.config['br'][1], 1)

    def turn_left(self):
        GPIO.output(self.config['al'][0], 0)
        GPIO.output(self.config['al'][1], 1)
        GPIO.output(self.config['ar'][0], 1)
        GPIO.output(self.config['ar'][1], 0)
        GPIO.output(self.config['bl'][0], 0)
        GPIO.output(self.config['bl'][1], 1)
        GPIO.output(self.config['br'][0], 1)
        GPIO.output(self.config['br'][1], 0)

    def turn_right(self):
        GPIO.output(self.config['al'][0], 1)
        GPIO.output(self.config['al'][1], 0)
        GPIO.output(self.config['ar'][0], 0)
        GPIO.output(self.config['ar'][1], 1)
        GPIO.output(self.config['bl'][0], 1)
        GPIO.output(self.config['bl'][1], 0)
        GPIO.output(self.config['br'][0], 0)
        GPIO.output(self.config['br'][1], 1)

    def stop(self):
        for index in self.config:
            GPIO.output(self.config[index][0], 0)
            GPIO.output(self.config[index][1], 0)
