from scape.signal.sensor import SignalSensor
from scape.signal.decorators import signal_func
import pygame


class Joystick(SignalSensor):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.joystick.init()

    @signal_func((1, ), (3, ), (4, ), (5, ), (6, ), (7, ), (8, ), (9, ))
    def press_buttons(self, index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()
        return joystick.get_button(index)

    @signal_func((0, ))
    def press_hats(self, index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()
        return joystick.get_hat(index)

    @signal_func((2, ), (3, ))
    def press_axes(self, index):
        if pygame.joystick.get_count() <= 0:
            return
        pygame.event.get()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        joystick.get_name()
        return joystick.get_axis(index)
