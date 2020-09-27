from scape.core.sensor import Sensor
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray


class Camera(Sensor):
    color_dic = {'black': [[(0, 0, 0), (180, 255, 46)]],
                 'grey': [[(0, 0, 46), (180, 43, 220)]],
                 'white': [[(0, 0, 221), (180, 30, 255)]],
                 'red': [[(0, 43, 46), (10, 255, 255)], [(156, 43, 46), (180, 255, 255)]],
                 'orange': [[(11, 43, 46), (25, 255, 255)]],
                 'yellow': [[(26, 43, 46), (34, 255, 255)]],
                 'green': [[(35, 43, 46), (77, 255, 255)]],
                 'cyan': [[(78, 43, 46), (99, 255, 255)]],
                 'blue': [[(100, 43, 46), (124, 255, 255)]],
                 'purple': [[(125, 43, 46), (155, 255, 255)]]}

    def __init__(self):
        super().__init__()
        self.camera = PiCamera()
        self.camera.resolution = (320, 240)
        self.camera.framerate = 60
        self.rawCapture = PiRGBArray(self.camera, size=(320, 240))

    def color_detective(self):
        frame = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)[0]
        img = frame.array
        size = img.shape[0] * img.shape[1]
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        max_color = ''
        max_percent = 0
        for color_name in self.color_dic:
            sum_size = 0
            for field in self.color_dic[color_name]:
                mask = cv2.inRange(hsv_img, field[0], field[1])
                binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
                binary = cv2.dilate(binary, None, iterations=2)
                cnt_s = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
                for c in cnt_s:
                    sum_size += cv2.contourArea(c)
            percent = round(sum_size / size, 2)
            if percent >= 0.80:
                print(color_name, ': ', percent)
                return color_name
            else:
                if percent >= max_percent:
                    max_percent = percent
                    max_color = color_name
        if max_color is not '':
            print(max_color, ': ', max_percent)
            return max_color
        return False
