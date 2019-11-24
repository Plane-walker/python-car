import RPi.GPIO as GPIO
GPIO.setmode(GIPO.BOARD)


def init_motor():
    # left_ahead
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    # right_ahead
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    # left_back
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    # right_back
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)


def go_ahead():
    GPIO.OUT(11, 1)
    GPIO.OUT(12, 0)
    GPIO.OUT(13, 1)
    GPIO.OUT(15, 0)
    GPIO.OUT(16, 1)
    GPIO.OUT(18, 0)
    GPIO.OUT(22, 1)
    GPIO.OUT(7, 0)


def go_back():
    GPIO.OUT(11, 0)
    GPIO.OUT(12, 1)
    GPIO.OUT(13, 0)
    GPIO.OUT(15, 1)
    GPIO.OUT(16, 0)
    GPIO.OUT(18, 1)
    GPIO.OUT(22, 0)
    GPIO.OUT(7, 1)


def turn_left():
    GPIO.OUT(11, 0)
    GPIO.OUT(12, 1)
    GPIO.OUT(13, 1)
    GPIO.OUT(15, 0)
    GPIO.OUT(16, 0)
    GPIO.OUT(18, 1)
    GPIO.OUT(22, 1)
    GPIO.OUT(7, 0)


def turn_right():
    GPIO.OUT(11, 1)
    GPIO.OUT(12, 0)
    GPIO.OUT(13, 0)
    GPIO.OUT(15, 1)
    GPIO.OUT(16, 1)
    GPIO.OUT(18, 0)
    GPIO.OUT(22, 0)
    GPIO.OUT(7, 1)


def stop():
    GPIO.OUT(11, 0)
    GPIO.OUT(12, 0)
    GPIO.OUT(13, 0)
    GPIO.OUT(15, 0)
    GPIO.OUT(16, 0)
    GPIO.OUT(18, 0)
    GPIO.OUT(22, 0)
    GPIO.OUT(7, 0)
