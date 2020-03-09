import RPi.GPIO as GPIO
from apps.config.config import motor_config
GPIO.setmode(GPIO.BOARD)


class Motor:
    def __init__(self):
        for index in motor_config:
            GPIO.setup(motor_config[index][0], GPIO.OUT)
            GPIO.setup(motor_config[index][1], GPIO.OUT)

    def go_ahead(self):
        for index in motor_config:
            GPIO.output(motor_config[index][0], 1)
            GPIO.output(motor_config[index][1], 0)

    def go_back(self):
        for index in motor_config:
            GPIO.output(motor_config[index][0], 0)
            GPIO.output(motor_config[index][1], 1)

    def go_left(self):
        GPIO.output(motor_config['al'][0], 1)
        GPIO.output(motor_config['al'][1], 0)
        GPIO.output(motor_config['ar'][0], 0)
        GPIO.output(motor_config['ar'][1], 1)
        GPIO.output(motor_config['bl'][0], 0)
        GPIO.output(motor_config['bl'][1], 1)
        GPIO.output(motor_config['br'][0], 1)
        GPIO.output(motor_config['br'][1], 0)

    def go_right(self):
        GPIO.output(motor_config['al'][0], 0)
        GPIO.output(motor_config['al'][1], 1)
        GPIO.output(motor_config['ar'][0], 1)
        GPIO.output(motor_config['ar'][1], 0)
        GPIO.output(motor_config['bl'][0], 1)
        GPIO.output(motor_config['bl'][1], 0)
        GPIO.output(motor_config['br'][0], 0)
        GPIO.output(motor_config['br'][1], 1)

    def turn_left(self):
        GPIO.output(motor_config['al'][0], 0)
        GPIO.output(motor_config['al'][1], 1)
        GPIO.output(motor_config['ar'][0], 1)
        GPIO.output(motor_config['ar'][1], 0)
        GPIO.output(motor_config['bl'][0], 0)
        GPIO.output(motor_config['bl'][1], 1)
        GPIO.output(motor_config['br'][0], 1)
        GPIO.output(motor_config['br'][1], 0)

    def turn_right(self):
        GPIO.output(motor_config['al'][0], 1)
        GPIO.output(motor_config['al'][1], 0)
        GPIO.output(motor_config['ar'][0], 0)
        GPIO.output(motor_config['ar'][1], 1)
        GPIO.output(motor_config['bl'][0], 1)
        GPIO.output(motor_config['bl'][1], 0)
        GPIO.output(motor_config['br'][0], 0)
        GPIO.output(motor_config['br'][1], 1)

    def stop(self):
        for index in motor_config:
            GPIO.output(motor_config[index][0], 0)
            GPIO.output(motor_config[index][1], 0)
