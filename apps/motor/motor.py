import RPi.GPIO as GPIO
from apps.config.config import Config
GPIO.setmode(GPIO.BOARD)


def init_motor():
    for index in Config.motor_pin:
        GPIO.setup(Config.motor_pin[index][0], GPIO.OUT)
        GPIO.setup(Config.motor_pin[index][1], GPIO.OUT)


def go_ahead():
    for index in Config.motor_pin:
        GPIO.output(Config.motor_pin[index][0], 1)
        GPIO.output(Config.motor_pin[index][1], 0)


def go_back():
    for index in Config.motor_pin:
        GPIO.output(Config.motor_pin[index][0], 0)
        GPIO.output(Config.motor_pin[index][1], 1)


def turn_left():
    GPIO.output(Config.motor_pin['al'][0], 0)
    GPIO.output(Config.motor_pin['al'][1], 1)
    GPIO.output(Config.motor_pin['ar'][0], 1)
    GPIO.output(Config.motor_pin['ar'][1], 0)
    GPIO.output(Config.motor_pin['bl'][0], 0)
    GPIO.output(Config.motor_pin['bl'][1], 1)
    GPIO.output(Config.motor_pin['br'][0], 1)
    GPIO.output(Config.motor_pin['br'][1], 0)


def turn_right():
    GPIO.output(Config.motor_pin['al'][0], 1)
    GPIO.output(Config.motor_pin['al'][1], 0)
    GPIO.output(Config.motor_pin['ar'][0], 0)
    GPIO.output(Config.motor_pin['ar'][1], 1)
    GPIO.output(Config.motor_pin['bl'][0], 1)
    GPIO.output(Config.motor_pin['bl'][1], 0)
    GPIO.output(Config.motor_pin['br'][0], 0)
    GPIO.output(Config.motor_pin['br'][1], 1)


def stop():
    for index in Config.motor_pin:
        GPIO.output(Config.motor_pin[index][0], 0)
        GPIO.output(Config.motor_pin[index][1], 0)
