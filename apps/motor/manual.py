import RPi.GPIO as GPIO


class Manual:
    config = {'al': [7, 11],
              'ar': [12, 13],
              'bl': [15, 16],
              'br': [18, 22]}
    
    def __init__(self):
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
