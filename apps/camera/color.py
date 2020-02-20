import cv2

from apps.config.config import color_dic


def video_stream():
    capture = cv2.VideoCapture(0)
    if capture.isOpened():
        f, img = capture.read()
        size = img.shape[0] * img.shape[1]
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        max_color = ''
        max_percent = 0
        for color_name in color_dic:
            sum_size = 0
            for field in color_dic[color_name]:
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
    capture.release()
    return False
