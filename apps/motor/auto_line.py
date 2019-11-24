import RPi.GPIO as GPIO
import time
from .motor import go_ahead, go_back, turn_left, turn_right
GPIO.setmode(GIPO.BOARD)

flag_l = 0
flag_r = 0


def adjust():
    global flag_l, flag_r
    if GPIO.getmode(29) > 0:
        flag_l = 1
        flag_r = 0
    if GPIO.getmode(37) > 0:
        flag_l = 0
        flag_r = 1

    '''锐角：根据flag记录的状态自转'''
    if GPIO.getmode(29) == 0 and GPIO.getmode(31) == 0 and GPIO.getmode(33) == 0 and GPIO.getmode(35) == 0 and GPIO.getmode(37) == 0:

        if flag_l == 1:
            turn_left()

        if flag_r == 1:
            turn_right()

    '''过十字'''
    if GPIO.getmode(29) > 0 and GPIO.getmode(31) > 0 and GPIO.getmode(33) > 0 and GPIO.getmode(35) > 0 and GPIO.getmode(37) > 0:
        go_ahead()
        time.sleep(0.02)

    '''中间传感器返回1走直线'''
    if GPIO.getmode(29) == 0 and GPIO.getmode(31) == 0 and GPIO.getmode(33) > 0 and GPIO.getmode(35) == 0 and GPIO.getmode(37) == 0:
        go_ahead()

    '''31返回1左转'''
    if GPIO.getmode(31) > 0:
        turn_left()

    '''35返回1右转'''
    if GPIO.getmode(31) > 0:
        turn_right()
