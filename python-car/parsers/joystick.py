from scape.core.parser import Parser
from scape.signal.signal import SignalFactory
from scape.action.action import ActionFactory


class Joystick(Parser):
    def __init__(self):
        super().__init__()
        self.automatic = False
        self.power = False
        for index in [1, 3, 4, 5, 6, 7, 8, 9]:
            self.add_rule(SignalFactory.make('Joystick.press_buttons', (index,)), self.buttons_rule)
        self.add_rule(SignalFactory.make('Joystick.press_hats', (0, )), self.hats_rule)
        self.add_rule(SignalFactory.make('right_axes'), self.axes_rule)
        self.init_activate(SignalFactory.make('Joystick.press_buttons', (9,)))

    def buttons_rule(self, signal, status):
        if status['new'] != 1:
            return
        args = signal.get_args()
        if args[0] == 1:
            return ActionFactory.make('Motor.turn_right', ())
        if args[0] == 3:
            return ActionFactory.make('Motor.turn_left', ())
        if args[0] == 4:
            return ActionFactory.make('Servo.servo_increase', (0,))
        if args[0] == 5:
            return ActionFactory.make('Servo.servo_decrease', (1,))
        if args[0] == 6:
            return ActionFactory.make('Servo.servo_decrease', (1,))
        if args[0] == 7:
            return ActionFactory.make('Servo.servo_increase', (0,))
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
        self.activate(SignalFactory.make('group_trace'))

    def deactivate_automatic(self):
        self.deactivate(SignalFactory.make('group_trace'))

    def activate_power(self):
        for index in [1, 3, 4, 5, 6, 7, 8]:
            self.activate(SignalFactory.make('Joystick.press_buttons', (index,)))
        self.activate(SignalFactory.make('Joystick.press_hats', (0,)))
        self.activate(SignalFactory.make('Joystick.press_axes', (2,)))
        self.activate(SignalFactory.make('Joystick.press_axes', (3,)))

    def deactivate_power(self):
        for index in [1, 3, 4, 5, 6, 7, 8]:
            self.deactivate(SignalFactory.make('Joystick.press_buttons', (index,)))
        self.deactivate(SignalFactory.make('Joystick.press_hats', (0,)))
        self.deactivate(SignalFactory.make('Joystick.press_axes', (2,)))
        self.deactivate(SignalFactory.make('Joystick.press_axes', (3,)))

    @staticmethod
    def hats_rule(signal, status):
        if status['new'][0] == 0 and status['new'][1] == 1:
            return ActionFactory.make('Servo.arm_ahead', ())
        if status['new'][0] == -1 and status['new'][1] == 0:
            return ActionFactory.make('Servo.arm_down', ())
        if status['new'][0] == 0 and status['new'][1] == -1:
            return ActionFactory.make('Servo.arm_back', ())
        if status['new'][0] == 1 and status['new'][1] == 0:
            return ActionFactory.make('Servo.arm_up', ())

    def axes_rule(self, signal, status):
        args = signal.get_args()
        if args[0] == 2:
            x_value = status['new']
            y_value = self.get_signal_status(SignalFactory.make('Joystick.press_axes', (3, )))['new']
        else:
            x_value = self.get_signal_status(SignalFactory.make('Joystick.press_axes', (2, )))['new']
            y_value = status['new']
        if abs(x_value) < 0.2 and abs(y_value) < 0.2:
            return ActionFactory.make('Motor.stop', ())
        if abs(x_value) > abs(y_value):
            if x_value > 0:
                return ActionFactory.make('Motor.go_right', ())
            else:
                return ActionFactory.make('Motor.go_left', ())
        else:
            if y_value > 0:
                return ActionFactory.make('Motor.go_ahead', ())
            else:
                return ActionFactory.make('Motor.go_back', ())
