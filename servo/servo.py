from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
servoInitAngle = [99, 99, 117, 144, 180]
servoNowAngle = servoInitAngle[:]
normalAngle = [123.1, 65.1, 29.6]
axisY = 10.0
axisZ = 12.0
carHeight = 16.06
pawHeight = 12.61
foreArm = 14.64
upperArm = 10.26

def set_servo_angle(channel, angle):
    date = int(4096 * ((angle * 11) + 500) / 20000)
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

def paw_open():
    if servoNowAngle[0] > 0:
        servoNowAngle[0] -= 5
    else:
        servoNowAngle[0] = 0
    set_servo_angle(0, servoNowAngle[0])

def cosine_law(side_a, side_b, side_c):
    return math.acos((side_c * side_c + side_b * side_b - side_a * side_a) / 2 / side_c / side_b) * 180 / 3.14159

def arm_move():
    sub_line = pow(axisY * axisY + (carHeight - axisZ - pawHeight) * (carHeight - axisZ - pawHeight), 0.5)
    servoNowAngle[3] += normalAngle[1] - cosine_law(sub_line, foreArm, upperArm)
    if carHeight - axisZ - pawHeight < 0:
        servoNowAngle[4] +=normalAngle[2] + 180 - (cosine_law(foreArm, sub_line, upperArm) + cosine_law(abs(carHeight - axisZ - pawHeight), axisY, sub_line))
        servoNowAngle[2] += cosine_law(upperArm, sub_line, foreArm) + cosine_law(axisY, abs(carHeight - axisZ - pawHeight), sub_line) - normalAngle[0]
    else:
        servoNowAngle[4] +=normalAngle[2] + 270 - (cosine_law(foreArm, sub_line, upperArm) + cosine_law(axisY, abs(carHeight - axisZ - pawHeight), sub_line))
        servoNowAngle[2] += cosine_law(upperArm, sub_line, foreArm) + cosine_law(abs(carHeight - axisZ - pawHeight), axisY, sub_line) + 90 - normalAngle[0]
    for index in [2, 3, 4]:
        if servoNowAngle[index] > 180:
            servoNowAngle[index] = 180
        elif servoNowAngle[index] < 0:
            servoNowAngle[index] = 0
        set_servo_angle(index, servoNowAngle[index])

def arm_up():
    global axisZ
    if axisZ < 22:
        axisZ += 1
    else:
        axisZ = 20
    arm_move()

def arm_down():
    global axisZ
    if axisZ > 3:
        axisZ -= 1
    else:
        axisZ = 3
    arm_move()

def arm_ahead():
    global axisY
    if axisY < 14:
        axisY += 1
    else:
        axisY = 14
    arm_move()

def arm_back():
    global axisY
    if axisY > 4:
        axisY -= 1
    else:
        axisY = 4
    arm_move()
