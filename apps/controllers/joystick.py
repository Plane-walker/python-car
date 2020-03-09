import pygame


class JoyStick:
    servo = None
    motor = None
    keyEvent = {
        'button_0': servo.servo_decrease,
        'button_1': servo.servo_decrease,
        'button_2': servo.servo_increase,
        'button_3': servo.servo_increase,
        'button_4': servo.arm_down,
        'button_5': servo.arm_up,
        'button_6': servo.arm_back,
        'button_7': servo.arm_ahead,
        'button_8': None,
        'button_9': None,
        'button_10': None,
        'button_11': None,
        'button_12': None,
        'button_13': None,
        'button_14': None,
        'hatX_0_hatY_0': motor.stop,
        'hatX_0_hatY_1': motor.go_ahead,
        'hatX_-1_hatY_0': None,
        'hatX_0_hatY_-1': None,
        'hatX_1_hatY_0': None,
        'axis': None
    }

    def __init__(self, servo, motor):
        pygame.init()
        pygame.joystick.init()
        self.button = [0] * 14
        self.hatX = 0
        self.hatY = 0
        self.axis = [0] * 6
        self.servo = servo
        self.motor = motor

    def joystick_control(self):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()

        axes = joystick.get_numaxes()
        for index in range(axes):
            axis_status = joystick.get_axis(index)
            if abs(self.axis[index] - axis_status) > 0.2:
                self.axis[index] = axis_status
                # print("Axis {} value: {:>6.3f}".format(index, axis[index]))

        buttons = joystick.get_numbuttons()
        for index in range(buttons):
            button_status = joystick.get_button(index)
            if self.button[index] is not button_status:
                self.button[index] = button_status
                if self.keyEvent['button_' + str(index)] is not None:
                    self.keyEvent['button_' + str(index)]()
                # print("Button {:>2} value: {}".format(index, button[index]))

        hats = joystick.get_numhats()
        for index in range(hats):
            hat_x_status, hat_y_status = joystick.get_hat(index)
            if self.hatX is not hat_x_status or self.hatY is not hat_y_status:
                self.hatX = hat_x_status
                self.hatY = hat_y_status
                if self.keyEvent['hatX_' + str(self.hatX) + '_hatY_' + str(self.hatY)] is not None:
                    self.keyEvent['hatX_' + str(self.hatX) + '_hatY_' + str(self.hatY)]()
                # print("Hat {} value: ({}, {})".format(index, hatX, hatY))
