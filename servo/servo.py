from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
servoNowAngle = [99, 99, 117, 144, 180]
normalAngle = [123.1, 65.1, 150.4]
axisX = 7.0
axisY = 14.0
carHeight = 16.06
pawHeight = 12.61
foreArm = 14.64
upperArm = 10.26


def circle_intersection(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((abs(x2 - x1)) ** 2 + (abs(y2 - y1)) ** 2)
    if d > (r1 + r2) or d < (abs(r1 - r2)):
        print ("Two circles have no intersection")
        return
    else:
        a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r1 ** 2 - a ** 2)
        x_temp = x1 + a * (x2 - x1)/d
        y_temp = y1 + a * (y2 - y1)/d
        x3 = round(x_temp - h * (y2 - y1) / d,2)
        y3 = round(y_temp + h * (x2 - x1) / d,2)
        # x4 = round(x_temp + h * (y2 - y1) / d,2)
        # y4 = round(y_temp - h * (x2 - x1) / d,2)
        return x3, y3

def cosine_law(x1, y1, x2, y2, x3, y3):
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x3 - x1
    dy2 = y3 - y1
    return math.acos((dx1 * dx2 + dy1 * dy2) / math.sqrt((dx1 ** 2 + dy1 ** 2) * (dx2 ** 2 + dy2 ** 2)))

def set_servo_angle(channel, angle):
    date = int(4096 * ((angle * 11) + 500) / 20000)
    pwm.set_pwm(channel, 0, date)

def init_servo_angle():
    for index in range(len(servoNowAngle)):
        set_servo_angle(index, servoNowAngle[index])
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

# def cosine_law(side_a, side_b, side_c):
#     return math.acos((side_c * side_c + side_b * side_b - side_a * side_a) / 2 / side_c / side_b) * 180 / 3.14159

def arm_move():
    # sub_line = pow(axisY * axisY + (carHeight - axisZ - pawHeight) * (carHeight - axisZ - pawHeight), 0.5)
    # servoNowAngle[3] += normalAngle[1] - cosine_law(sub_line, foreArm, upperArm)
    # if carHeight - axisZ - pawHeight < 0:
    #     servoNowAngle[4] +=normalAngle[2] + 180 - (cosine_law(foreArm, sub_line, upperArm) + cosine_law(abs(carHeight - axisZ - pawHeight), axisY, sub_line))
    #     servoNowAngle[2] += cosine_law(upperArm, sub_line, foreArm) + cosine_law(axisY, abs(carHeight - axisZ - pawHeight), sub_line) - normalAngle[0]
    # else:
    #     servoNowAngle[4] +=normalAngle[2] + 270 - (cosine_law(foreArm, sub_line, upperArm) + cosine_law(axisY, abs(carHeight - axisZ - pawHeight), sub_line))
    #     servoNowAngle[2] += cosine_law(upperArm, sub_line, foreArm) + cosine_law(abs(carHeight - axisZ - pawHeight), axisY, sub_line) + 90 - normalAngle[0]
    inter_x, inter_y = circle_intersection(0, 0, upperArm, axisX, axisY, foreArm)
    servoNowAngle[2] += cosine_law(axisX, axisY, inter_x, inter_y, 0, 0) - normalAngle[0]
    normalAngle[0] = cosine_law(axisX, axisY, inter_x, inter_y, 0, 0)
    servoNowAngle[3] += normalAngle[1] - cosine_law(inter_x, inter_y, 0, 0, axisX, axisY)
    normalAngle[1] = cosine_law(inter_x, inter_y, 0, 0, axisX, axisY)
    servoNowAngle[4] += normalAngle[2] - cosine_law(0, 0, inter_x, inter_y, axisX, axisY)
    normalAngle[2] = cosine_law(0, 0, inter_x, inter_y, axisX, axisY)
    for index in [2, 3, 4]:
        if servoNowAngle[index] > 180:
            servoNowAngle[index] = 180
        elif servoNowAngle[index] < 0:
            servoNowAngle[index] = 0
        set_servo_angle(index, servoNowAngle[index])

def arm_up():
    global axisY
    if axisY < 22:
        axisY += 1
    else:
        axisY = 22
    arm_move()

def arm_down():
    global axisY
    if axisY > 3:
        axisY -= 1
    else:
        axisY = 3
    arm_move()

def arm_ahead():
    global axisX
    if axisX < 14:
        axisX += 1
    else:
        axisX = 14
    arm_move()

def arm_back():
    global axisX
    if axisX > 4:
        axisX -= 1
    else:
        axisX = 4
    arm_move()
