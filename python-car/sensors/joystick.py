from scape.core.sensor import Sensor
import pygame


class Joystick(Sensor):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.joystick.init()
        pygame.event.get()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def press_buttons(self, index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        return self.joystick.get_button(index)

    def press_hats(self, index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        return self.joystick.get_hat(index)

    def press_axes(self, index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        return self.joystick.get_axis(index)


class RightAxes(Joystick):
    def __init__(self):
        super().__init__()

    def push(self):
        return self.press_axes(2), self.press_axes(3)
