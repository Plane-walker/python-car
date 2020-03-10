import threading
from apps.controllers.interface import Controllers


def main():
    controller = Controllers()
    # video_thread = threading.Thread(target=video_stream)
    # video_thread.setDaemon(True)
    # video_thread.start()
    # screen = pygame.display.set_mode(640, 480)

    while True:
        controller.run()


if __name__ == '__main__':
    main()
