from scape.core.parser import Parser
from scape.event.action import ActionFactory
from scape.event.signal import SignalFactory


class Automatic(Parser):
    def __init__(self):
        super().__init__()
        self.flag_l = 0
        self.flag_r = 0
        self.add_rule(SignalFactory.make('GroupTrace.detective_group'), self.adjust)

    def adjust(self):
        signal = self.received_signal()
        status = signal.get_status()
        if not status['new'][0]:
            self.flag_l = 1
            self.flag_r = 0
        if not status['new'][4]:
            self.flag_l = 0
            self.flag_r = 1

        '''锐角：根据flag记录的状态自转'''
        if status['new'][0] == 0 and status['new'][1] == 0 and status['new'][2] == 0 and status['new'][3] == 0 and status['new'][4] == 0:
            if self.flag_l == 1:
                return ActionFactory.make('Motor.turn_left', ())

            if self.flag_r == 1:
                return ActionFactory.make('Motor.turn_right', ())

        '''过十字'''
        if status['new'][0] == 1 and status['new'][1] == 1 and status['new'][2] == 1 and status['new'][3] == 1 and status['new'][4] == 1:
            return ActionFactory.make('Motor.go_ahead', ())

        '''中间传感器返回1走直线'''
        if status['new'][0] == 0 and status['new'][1] == 0 and status['new'][2] == 1 and status['new'][3] == 0 and status['new'][4] == 0:
            return ActionFactory.make('Motor.go_ahead', ())

        '''31返回1左转'''
        if status['new'][1] == 1:
            return ActionFactory.make('Motor.turn_left', ())

        '''35返回1右转'''
        if status['new'][1] == 1:
            return ActionFactory.make('Motor.turn_right', ())
