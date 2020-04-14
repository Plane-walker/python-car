from scape.core.parser import Parser


class Joystick(Parser):
    def __init__(self):
        super().__init__()
        self.automatic = False
        self.power = False
        self.add_rule('Joystick.press_buttons', self.buttons_rule)
        self.add_rule(('Joystick.press_hats', (0, )), self.hats_rule)
        self.add_multi_signal_rule(('Joystick.press_axes', (2, )), self.axes_rule)
        self.add_multi_signal_rule(('Joystick.press_axes', (3, )), self.axes_rule)

    def buttons_rule(self, args, status):
        if status['new'] != 1:
            return
        if args[0] == 1:
            return 'Motor.turn_right', ()
        if args[0] == 3:
            return 'Motor.turn_left', ()
        if args[0] == 4:
            return 'Servo.servo_increase', (0,)
        if args[0] == 5:
            return 'Servo.servo_decrease', (1,)
        if args[0] == 6:
            return 'Servo.servo_decrease', (1,)
        if args[0] == 7:
            return 'Servo.servo_increase', (0,)
        if args[0] == 8:
            if status['old'] == 0:
                if not self.automatic:
                    self.activate_automatic()
                else:
                    self.deactivate_automatic()
                self.automatic = not self.automatic
        if args[0] == 9:
            if status['old'] == 0:
                if not self.power:
                    self.activate_power()
                else:
                    self.deactivate_power()
                self.power = not self.power

    def activate_automatic(self):
        pass

    def deactivate_automatic(self):
        pass

    def activate_power(self):
        self.activate('Joystick.press_buttons', (1, ))
        self.activate('Joystick.press_buttons', (3, ))
        self.activate('Joystick.press_buttons', (4, ))
        self.activate('Joystick.press_buttons', (5, ))
        self.activate('Joystick.press_buttons', (6, ))
        self.activate('Joystick.press_buttons', (7, ))
        self.activate('Joystick.press_buttons', (8, ))
        self.activate('Joystick.press_hats', (0, ))
        self.activate('Joystick.press_axes', (2, ))
        self.activate('Joystick.press_axes', (3, ))

    def deactivate_power(self):
        self.deactivate('Joystick.press_buttons', (1,))
        self.deactivate('Joystick.press_buttons', (3,))
        self.deactivate('Joystick.press_buttons', (4,))
        self.deactivate('Joystick.press_buttons', (5,))
        self.deactivate('Joystick.press_buttons', (6,))
        self.deactivate('Joystick.press_buttons', (7,))
        self.deactivate('Joystick.press_buttons', (8,))
        self.deactivate('Joystick.press_hats', (0,))
        self.deactivate('Joystick.press_axes', (2,))
        self.deactivate('Joystick.press_axes', (3,))

    @staticmethod
    def hats_rule(args, status):
        if status['new'][0] == 0 and status['new'][1] == 1:
            return 'Servo.arm_ahead', ()
        if status['new'][0] == -1 and status['new'][1] == 0:
            return 'Servo.arm_down', ()
        if status['new'][0] == 0 and status['new'][1] == -1:
            return 'Servo.arm_back', ()
        if status['new'][0] == 1 and status['new'][1] == 0:
            return 'Servo.arm_up', ()

    def axes_rule(self, args, status):
        if args[0] == 2:
            x_value = status['new']
            y_value = self.get_status('Joystick.press_axes', (3, ))['new']
        else:
            x_value = self.get_status('Joystick.press_axes', (2, ))['new']
            y_value = status['new']
        if abs(x_value) < 0.2 and abs(y_value) < 0.2:
            return 'Motor.stop', ()
        if abs(x_value) > abs(y_value):
            if x_value > 0:
                return 'Motor.go_right', ()
            else:
                return 'Motor.go_left', ()
        else:
            if y_value > 0:
                return 'Motor.go_ahead', ()
            else:
                return 'Motor.go_back', ()
