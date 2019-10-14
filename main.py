import pygame
from apps.servo.servo import init_servo_angle
from apps.controlers.joystick import joystick_control

pygame.init()
pygame.joystick.init()
init_servo_angle()

while True:
    while pygame.joystick.get_count() > 0:
        joystick_control()
    # while

