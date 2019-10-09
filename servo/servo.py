from __future__ import division
import time
import math
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
servoNowAngle = [99, 99, 117, 144, 180]
normalAngle = [65.1, 150.4]
axisX = 7.0
axisY = 14.0
carHeight = 16.06
pawHeight = 12.61
foreArm = 14.64
upperArm = 10.26


def circle_intersection(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((abs(x2 - x1)) ** 2 + (abs(y2 - y1)) ** 2)
    if d > (r1 + r2) or d < (abs(r1 - r2)):
        return 0, 0
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
    return math.acos((dx1 * dx2 + dy1 * dy2) / math.sqrt((dx1 ** 2 + dy1 ** 2) * (dx2 ** 2 + dy2 ** 2))) * 180 / 3.14159

def set_servo_angle(channel, angle):
    date = int(4096 * ((angle * 11) + 500) / 20000)
    pwm.set_pwm(channel, 0, date)

def init_servo_angle():
    for index in range(len(servoNowAngle)):
        set_servo_angle(index, servoNowAngle[index])
        time.sleep(1)

def paw_close():
    if servoNowAngle[0] < 180:
        servoNowAngle[0] += 3
    else:
        servoNowAngle[0] = 180
    set_servo_angle(0, servoNowAngle[0])

def paw_open():
    if servoNowAngle[0] > 0:
        servoNowAngle[0] -= 3
    else:
        servoNowAngle[0] = 0
    set_servo_angle(0, servoNowAngle[0])

def paw_up():
    if servoNowAngle[1] < 180:
        servoNowAngle[1] += 3
    else:
        servoNowAngle[1] = 180
    set_servo_angle(1, servoNowAngle[1])

def paw_down():
    if servoNowAngle[1] > 0:
        servoNowAngle[1] -= 3
    else:
        servoNowAngle[1] = 0
    set_servo_angle(1, servoNowAngle[1])

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
    if inter_x == 0 and inter_y == 0:
        return -1
    servoNowAngle[3] += normalAngle[0] - cosine_law(inter_x, inter_y, 0, 0, axisX, axisY)
    normalAngle[0] = cosine_law(inter_x, inter_y, 0, 0, axisX, axisY)
    servoNowAngle[4] += cosine_law(0, 0, inter_x, inter_y, 1, 0) - normalAngle[1]
    normalAngle[1] = cosine_law(0, 0, inter_x, inter_y, 1, 0)
    if 0 <= servoNowAngle[3] <= 180 and 0 <= servoNowAngle[4] <= 180:
        set_servo_angle(3, servoNowAngle[3])
        set_servo_angle(4, servoNowAngle[4])
    else:
        return -1
    return 0

def arm_up():
    global axisY
    axisY += 1
    status = arm_move()
    if status == -1:
        axisY -= 1
        return "CAN'T REACH"
    return "OK"

def arm_down():
    global axisY
    axisY -= 1
    status = arm_move()
    if status == -1:
        axisY += 1
        return "CAN'T REACH"
    return "OK"

def arm_ahead():
    global axisX
    axisX += 1
    status = arm_move()
    if status == -1:
        axisX += 1
        return "CAN'T REACH"
    return "OK"

def arm_back():
    global axisX
    axisX -= 1
    status = arm_move()
    if status == -1:
        axisX += 1
        return "CAN'T REACH"
    return "OK"
