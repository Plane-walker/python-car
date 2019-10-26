import pygame
import threading
from apps.servo.servo import init_servo_angle
from apps.controlers.joystick import joystick_control
# from apps.controlers.keyboard import keyboard_control
from apps.camera.camera import video_stream

pygame.init()
pygame.joystick.init()
init_servo_angle()
video_thread = threading.Thread(target=video_stream)
video_thread.setDaemon(True)
video_thread.start()
# screen = pygame.display.set_mode(640, 480)

while True:
    if pygame.joystick.get_count() > 0:
        joystick_control()
    # else:
    #     keyboard_control()
