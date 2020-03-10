import time
from apps.sensor.trace import Trace


class Automatic:
    def __init__(self, motor):
        self.motor = motor
        self.trace = Trace()
        self.flag_l = 0
        self.flag_r = 0

    def adjust(self):
        if not self.trace.is_0(0):
            self.flag_l = 1
            self.flag_r = 0
        if not self.trace.is_0(4):
            self.flag_l = 0
            self.flag_r = 1

        '''锐角：根据flag记录的状态自转'''
        if self.trace.all_0():

            if self.flag_l == 1:
                self.motor.turn_left()

            if self.flag_r == 1:
                self.motor.turn_right()

        '''过十字'''
        if self.trace.all_1():
            self.motor.go_ahead()
            time.sleep(0.02)

        '''中间传感器返回1走直线'''
        if self.trace.assume_0({0: 0, 1: 0, 2: 1, 3: 0, 4: 0}):
            self.motor.go_ahead()

        '''31返回1左转'''
        if not self.trace.is_0(1):
            self.motor.turn_left()

        '''35返回1右转'''
        if not self.trace.is_0(1):
            self.motor.turn_right()
