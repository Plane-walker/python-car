import pygame
from servo.servo import paw_close, paw_open

button = [0] * 14
hatX = 0
hatY = 0
axis = [0] * 6

pygame.init()
pygame.joystick.init()

while True:
    pygame.event.get()
    joystickCount = pygame.joystick.get_count()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    name = joystick.get_name()

    axes = joystick.get_numaxes()
    for index in range(axes):
        axisStatus = joystick.get_axis(index)
        if abs(axis[index] - axisStatus) > 0.2:
            axis[index] = axisStatus
            print("Axis {} value: {:>6.3f}".format(index, axis[index]))

    buttons = joystick.get_numbuttons()
    for index in range(buttons):
        buttonStatus = joystick.get_button(index)
        if button[index] is not buttonStatus:
            button[index] = buttonStatus
            print("Button {:>2} value: {}".format(index, button[index]))

    hats = joystick.get_numhats()
    for index in range(hats):
            hatXStatus, hatYStatus = joystick.get_hat(index)
            if hatX is not hatXStatus or hatY is not hatYStatus:
                hatX = hatXStatus
                hatY = hatYStatus
                print("Hat {} value: ({}, {})".format(index, hatX, hatY))

    if button[2] == 1:
        paw_close()

    if button[0] == 1:
        paw_open()
