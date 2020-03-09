import threading
from apps.controllers.interface import Controllers
# from apps.controllers.keyboard import keyboard_control
# from apps.camera.color import color_detective
from apps.motor.motor import init_motor


def main():
    controller = Controllers()
    init_motor()
    # video_thread = threading.Thread(target=video_stream)
    # video_thread.setDaemon(True)
    # video_thread.start()
    # screen = pygame.display.set_mode(640, 480)

    while True:
        controller.run()


if __name__ == '__main__':
    main()
