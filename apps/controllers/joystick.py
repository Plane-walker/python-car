import pygame


class JoyStick:
    def __init__(self, servo, motor):
        pygame.init()
        pygame.joystick.init()
        self.button = [0] * 14
        self.hatX = 0
        self.hatY = 0
        self.axis = [0] * 6
        self.servo = servo
        self.motor = motor
        self.keyEvent = {
            'button_0': [None, ()],
            'button_1': [motor.turn_right, ()],
            'button_2': [None, ()],
            'button_3': [motor.turn_left, ()],
            'button_4': [servo.servo_increase, (0,)],
            'button_5': [servo.servo_decrease, (1,)],
            'button_6': [servo.servo_decrease, (1,)],
            'button_7': [servo.servo_increase, (0,)],
            'button_8': [None, ()],
            'button_9': [None, ()],
            'button_10': [None, ()],
            'button_11': [None, ()],
            'button_12': [None, ()],
            'button_13': [None, ()],
            'button_14': [None, ()],
            'hatX_0_hatY_0': [None, ()],
            'hatX_1_hatY_1': [None, ()],
            'hatX_1_hatY_-1': [None, ()],
            'hatX_-1_hatY_1': [None, ()],
            'hatX_0_hatY_1': [servo.arm_ahead, ()],
            'hatX_-1_hatY_0': [servo.arm_down, ()],
            'hatX_0_hatY_-1': [servo.arm_back, ()],
            'hatX_1_hatY_0': [servo.arm_up, ()],
            'axis_0': [None, ()],
            'axis_1': [self.go_movement, ()],
            'axis_2': [None, ()]
        }

    def go_movement(self):
        if abs(self.axis[2]) < 0.2 and abs(self.axis[3]) < 0.2:
            self.motor.stop()
        elif abs(self.axis[2]) > abs(self.axis[3]):
            if self.axis[2] > 0:
                self.motor.go_right()
            else:
                self.motor.go_left()
        else:
            if self.axis[3] > 0:
                self.motor.go_ahead()
            else:
                self.motor.go_back()

    def joystick_control(self):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()

        axes = joystick.get_numaxes()
        update = [False] * (axes / 2)
        for index in range(axes):
            axis_status = joystick.get_axis(index)
            if abs(self.axis[index] - axis_status) > 0.2:
                self.axis[index] = axis_status
                update[index // 2] = True
                # print("Axis {} value: {:>6.3f}".format(index, axis[index]))
        for index in range(axes / 2):
            if update[index]:
                if self.keyEvent['axes_' + str(index)][0] is not None:
                    args = self.keyEvent['axes_' + str(index)][1]
                    self.keyEvent['axes_' + str(index)][0](*args)

        buttons = joystick.get_numbuttons()
        for index in range(buttons):
            button_status = joystick.get_button(index)
            if self.button[index] is not button_status:
                self.button[index] = button_status
                if self.keyEvent['button_' + str(index)][0] is not None:
                    args = self.keyEvent['button_' + str(index)][1]
                    self.keyEvent['button_' + str(index)][0](*args)
                # print("Button {:>2} value: {}".format(index, button[index]))

        hats = joystick.get_numhats()
        for index in range(hats):
            hat_x_status, hat_y_status = joystick.get_hat(index)
            if self.hatX is not hat_x_status or self.hatY is not hat_y_status:
                self.hatX = hat_x_status
                self.hatY = hat_y_status
                if self.keyEvent['hatX_' + str(self.hatX) + '_hatY_' + str(self.hatY)][0] is not None:
                    args = self.keyEvent['hatX_' + str(self.hatX) + '_hatY_' + str(self.hatY)][1]
                    self.keyEvent['hatX_' + str(self.hatX) + '_hatY_' + str(self.hatY)][0](*args)
                # print("Hat {} value: ({}, {})".format(index, hatX, hatY))
