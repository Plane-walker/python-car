from scape.signal.sensor import SignalSensor
from scape.signal.decorators import signal_func
import pygame


class Joystick(SignalSensor):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.joystick.init()

    @staticmethod
    def press_buttons(index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()
        return joystick.get_button(index)

    @staticmethod
    def press_hats(index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()
        return joystick.get_hat(index)

    @staticmethod
    def press_axes(index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()
        return joystick.get_axis(index)
