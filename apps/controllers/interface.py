from .joystick import JoyStick
from apps.servo.servo import Servo
from apps.motor.motor import Motor


class Controllers:
    def __init__(self):
        self.servo = Servo()
        self.motor = Motor()
        self.joy_stick = JoyStick(self.servo, self.motor)

    def run(self):
        self.joy_stick.joystick_control()
