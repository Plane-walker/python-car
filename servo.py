from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
servoInitAngle = [99, 99, 117, 144, 180]
servoNowAngle = servoInitAngle[:]

def set_servo_angle(channel, angle):
    date = 4096 * ((angle * 11) + 500) / 20000
    pwm.set_pwm(channel, 0, date)

def init_servo_angle():
    for index in range(len(servoInitAngle)):
        set_servo_angle(index, servoInitAngle[index])
        time.sleep(1)

def paw_close():
    if servoNowAngle[0] < 2500:
        servoNowAngle[0] += 5
    else:
        servoNowAngle[0] = 2500
    set_servo_angle(0, servoNowAngle[0])