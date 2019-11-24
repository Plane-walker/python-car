import RPi.GPIO as GPIO
GPIO.setmode(GIPO.BOARD)


def init_trace():
    GPIO.setup(29, GPIO.IN)
    GPIO.setup(31, GPIO.IN)
    GPIO.setup(33, GPIO.IN)
    GPIO.setup(35, GPIO.IN)
    GPIO.setup(37, GPIO.IN)
