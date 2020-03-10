from apps.controllers.joystick import JoyStick
from apps.servo.servo import Servo
from apps.motor.manual import Manual


class Controllers:
    def __init__(self):
        self.servo = Servo()
        self.motor = Manual()
        self.joy_stick = JoyStick(self.servo, self.motor)

    def run(self):
        self.joy_stick.joystick_control()
