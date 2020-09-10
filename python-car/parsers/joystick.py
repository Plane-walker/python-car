from scape.core.parser import Parser
from scape.signal.signal import SignalFactory
from scape.action.action import ActionFactory


class Joystick(Parser):
    def __init__(self):
        super().__init__()
        self.automatic = False
        self.power = False
        for index in [1, 3, 4, 5, 6, 7]:
            self.add_rule(SignalFactory.make('Joystick.press_buttons', (index,)), self.buttons_rule)
        self.add_rule(SignalFactory.make('Joystick.press_buttons', (8,)), self.automatic_button_rule)
        self.add_rule(SignalFactory.make('Joystick.press_buttons', (9,)), self.power_button_rule)
        self.add_rule(SignalFactory.make('Joystick.press_hats', (0, )), self.hats_rule)
        self.add_rule(SignalFactory.make('right_axes'), self.axes_rule)
        self.process(ActionFactory.make('Activator.init_activate', SignalFactory.make('Joystick.press_buttons', (9,))))

    def buttons_rule(self):
        signal = self.received_signal()
        status = signal.get_status()
        if status['new'] != 1:
            return
        args = signal.get_args()
        if args[0] == 1:
            self.process(ActionFactory.make('Motor.turn_right', ()))
        elif args[0] == 3:
            self.process(ActionFactory.make('Motor.turn_left', ()))
        elif args[0] == 4:
            self.process(ActionFactory.make('Servo.servo_increase', (0,)))
        elif args[0] == 5:
            self.process(ActionFactory.make('Servo.servo_decrease', (1,)))
        elif args[0] == 6:
            self.process(ActionFactory.make('Servo.servo_decrease', (1,)))
        elif args[0] == 7:
            self.process(ActionFactory.make('Servo.servo_increase', (0,)))

    def power_button_rule(self):
        signal = self.received_signal()
        status = signal.get_status()
        if status['old'] == 0:
            if not self.power:
                self.activate_power()
            else:
                self.deactivate_power()
            self.power = not self.power

    def automatic_button_rule(self):
        signal = self.received_signal()
        status = signal.get_status()
        if status['old'] == 0:
            if not self.automatic:
                self.activate_automatic()
            else:
                self.deactivate_automatic()
            self.automatic = not self.automatic

    def activate_automatic(self):
        self.process(ActionFactory.make('Activator.activate', SignalFactory.make('group_trace')))
        for index in [1, 3, 4, 5, 6, 7]:
            self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('Joystick.press_buttons', (index,))))
        self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('Joystick.press_hats', (0,))))
        self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('right_axes')))

    def deactivate_automatic(self):
        self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('group_trace')))
        for index in [1, 3, 4, 5, 6, 7]:
            self.process(ActionFactory.make('Activator.activate', SignalFactory.make('Joystick.press_buttons', (index,))))
        self.process(ActionFactory.make('Activator.activate', SignalFactory.make('Joystick.press_hats', (0,))))
        self.process(ActionFactory.make('Activator.activate', SignalFactory.make('right_axes')))

    def activate_power(self):
        for index in [1, 3, 4, 5, 6, 7, 8]:
            self.process(ActionFactory.make('Activator.activate', SignalFactory.make('Joystick.press_buttons', (index,))))
        self.process(ActionFactory.make('Activator.activate', SignalFactory.make('Joystick.press_hats', (0,))))
        self.process(ActionFactory.make('Activator.activate', SignalFactory.make('right_axes')))

    def deactivate_power(self):
        for index in [1, 3, 4, 5, 6, 7, 8]:
            self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('Joystick.press_buttons', (index,))))
        self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('Joystick.press_hats', (0,))))
        self.process(ActionFactory.make('Activator.deactivate', SignalFactory.make('right_axes')))

    def hats_rule(self):
        signal = self.received_signal()
        status = signal.get_status()
        if status['new'][0] == 0 and status['new'][1] == 1:
            self.process(ActionFactory.make('Servo.arm_ahead', ()))
        elif status['new'][0] == -1 and status['new'][1] == 0:
            self.process(ActionFactory.make('Servo.arm_down', ()))
        elif status['new'][0] == 0 and status['new'][1] == -1:
            self.process(ActionFactory.make('Servo.arm_back', ()))
        elif status['new'][0] == 1 and status['new'][1] == 0:
            self.process(ActionFactory.make('Servo.arm_up', ()))

    def axes_rule(self):
        signal = self.received_signal()
        status = signal.get_status()
        x_value = status[0]['new']
        y_value = status[1]['new']
        if abs(x_value) < 0.2 and abs(y_value) < 0.2:
            self.process(ActionFactory.make('Motor.stop', ()))
        elif abs(x_value) > abs(y_value):
            if x_value > 0:
                self.process(ActionFactory.make('Motor.go_right', ()))
            else:
                self.process(ActionFactory.make('Motor.go_left', ()))
        else:
            if y_value > 0:
                self.process(ActionFactory.make('Motor.go_ahead', ()))
            else:
                self.process(ActionFactory.make('Motor.go_back', ()))
