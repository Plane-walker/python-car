import pygame
from ..servo.servo import servo_increase, servo_decrease, arm_ahead, arm_back, arm_up, arm_down

def keyboard_control():
    pygame.event.get()
    key_list = pygame.key.get_pressed()
# paw function
    if key_list[pygame.K_e]:
        servo_increase(0)
    if key_list[pygame.K_q]:
        servo_decrease(0)

# arm function
    if key_list[pygame.K_UP]:
        arm_up()

    if key_list[pygame.K_DOWN]:
        arm_down()

    if key_list[pygame.K_LEFT]:
        arm_ahead()

    if key_list[pygame.K_RIGHT]:
        arm_back()
    pygame.event.pump()
    pygame.time.delay(10)