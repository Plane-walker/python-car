import pygame

button = [0] * 14
hat = [0, 0]
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

    #hats = joystick.get_numhats()
    #for index in range(hats):
            #hat = joystick.get_hat(index)
            #print("Hat {} value: {}".format(i, str(hat)))
