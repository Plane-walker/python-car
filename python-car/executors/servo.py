from scape.action.executor import ActionExecutor
import time
import Adafruit_PCA9685
import math


def circle_intersection(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((abs(x2 - x1)) ** 2 + (abs(y2 - y1)) ** 2)
    if d > (r1 + r2) or d < (abs(r1 - r2)):
        return 0, 0
    else:
        a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r1 ** 2 - a ** 2)
        x_temp = x1 + a * (x2 - x1)/d
        y_temp = y1 + a * (y2 - y1)/d
        x3 = round(x_temp - h * (y2 - y1) / d, 2)
        y3 = round(y_temp + h * (x2 - x1) / d, 2)
        # x4 = round(x_temp + h * (y2 - y1) / d,2)
        # y4 = round(y_temp - h * (x2 - x1) / d,2)
        return x3, y3


def cosine_law(x1, y1, x2, y2, x3, y3):
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x3 - x1
    dy2 = y3 - y1
    return round(math.acos((dx1 * dx2 + dy1 * dy2) / math.sqrt((dx1 ** 2 + dy1 ** 2) * (dx2 ** 2 + dy2 ** 2))) * 180 / math.pi, 2)


class Servo(ActionExecutor):
    def __init__(self):
        super().__init__()
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)
        self.config = {'height': 16.06,
                       'paw_height': 12.61,
                       'fore_arm_length': 14.64,
                       'upper_arm_length': 10.26,
                       'servo_angle': [99, 99, 117, 144, 180],
                       'angle': [65.1, 150.4]}
        self.axisX = 7.0
        self.axisY = 14.0
        for index in range(len(self.config['servo_angle'])):
            self.set_servo_angle(index, self.config['servo_angle'][index])
            time.sleep(1)

    def set_servo_angle(self, channel, angle):
        date = int(4096 * ((angle * 11) + 500) / 20000)
        self.pwm.set_pwm(channel, 0, date)

    def servo_increase(self, index):
        if self.config['servo_angle'][index] < 180:
            self.config['servo_angle'][index] += 3
        else:
            self.config['servo_angle'][index] = 180
        self.set_servo_angle(index, self.config['servo_angle'][index])

    def servo_decrease(self, index):
        if self.config['servo_angle'][index] > 0:
            self.config['servo_angle'][index] -= 3
        else:
            self.config['servo_angle'][index] = 0
        self.set_servo_angle(index, self.config['servo_angle'][index])

    def arm_move(self):
        inter_x, inter_y = circle_intersection(0, 0, self.config['upper_arm_length'], self.axisX, self.axisY, self.config['fore_arm_length'])
        if inter_x == 0 and inter_y == 0:
            return -1
        self.config['servo_angle'][3] += self.config['angle'][0] - cosine_law(inter_x, inter_y, 0, 0, self.axisX, self.axisY)
        self.config['angle'][0] = cosine_law(inter_x, inter_y, 0, 0, self.axisX, self.axisY)
        self.config['servo_angle'][4] += cosine_law(0, 0, inter_x, inter_y, 1, 0) - self.config['angle'][1]
        self.config['angle'][1] = cosine_law(0, 0, inter_x, inter_y, 1, 0)
        if 0 <= self.config['servo_angle'][3] <= 180 and 0 <= self.config['servo_angle'][4] <= 180:
            self.set_servo_angle(3, self.config['servo_angle'][3])
            self.set_servo_angle(4, self.config['servo_angle'][4])
        else:
            return -1
        return 0

    def arm_up(self):
        self.axisY += 1
        status = self.arm_move()
        if status == -1:
            self.axisY -= 1
            return "CAN'T REACH"
        return "OK"

    def arm_down(self):
        self.axisY -= 1
        status = self.arm_move()
        if status == -1:
            self.axisY += 1
            return "CAN'T REACH"
        return "OK"

    def arm_ahead(self):
        self.axisX += 1
        status = self.arm_move()
        if status == -1:
            self.axisX -= 1
            return "CAN'T REACH"
        return "OK"

    def arm_back(self):
        self.axisX -= 1
        status = self.arm_move()
        if status == -1:
            self.axisX += 1
            return "CAN'T REACH"
        return "OK"
