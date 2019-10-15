import pygame
from ..servo.servo import servo_increase, servo_decrease, arm_ahead, arm_back, arm_up, arm_down

button = [0] * 14
hatX = 0
hatY = 0
axis = [0] * 6

def joystick_control():
    pygame.event.get()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    name = joystick.get_name()

    axes = joystick.get_numaxes()
    for index in range(axes):
        axis_status = joystick.get_axis(index)
        if abs(axis[index] - axis_status) > 0.2:
            axis[index] = axis_status
            # print("Axis {} value: {:>6.3f}".format(index, axis[index]))

    buttons = joystick.get_numbuttons()
    for index in range(buttons):
        button_status = joystick.get_button(index)
        if button[index] is not button_status:
            button[index] = button_status
            # print("Button {:>2} value: {}".format(index, button[index]))

    hats = joystick.get_numhats()
    for index in range(hats):
            hat_x_status, hat_y_status = joystick.get_hat(index)
            global hatX, hatY
            if hatX is not hat_x_status or hatY is not hat_y_status:
                hatX = hat_x_status
                hatY = hat_y_status
                #print("Hat {} value: ({}, {})".format(index, hatX, hatY))

# paw function
    if button[2] == 1:
        servo_decrease(0)

    if button[0] == 1:
        servo_increase(0)

# arm function
    if button[5] == 1:
        arm_up()

    if button[4] == 1:
        arm_down()

    if button[7] == 1:
        arm_ahead()

    if button[6] == 1:
        arm_back()