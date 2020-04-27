from scape.core.parser import Parser
from scape.action.action import ActionFactory
from scape.signal.signal import SignalFactory


class Automatic(Parser):
    def __init__(self):
        super().__init__()
        self.flag_l = 0
        self.flag_r = 0
        self.add_rule(SignalFactory.make('group_trace'), self.adjust)

    def adjust(self, signal, status):
        if not status[0]['new']:
            self.flag_l = 1
            self.flag_r = 0
        if not status[4]['new']:
            self.flag_l = 0
            self.flag_r = 1

        '''锐角：根据flag记录的状态自转'''
        if status[0]['new'] == 0 and status[1]['new'] == 0 and status[2]['new'] == 0 and status[3]['new'] == 0 and status[4]['new'] == 0:
            if self.flag_l == 1:
                return ActionFactory.make('Motor.turn_left', ())

            if self.flag_r == 1:
                return ActionFactory.make('Motor.turn_right', ())

        '''过十字'''
        if status[0]['new'] == 1 and status[1]['new'] == 1 and status[2]['new'] == 1 and status[3]['new'] == 1 and status[4]['new'] == 1:
            return ActionFactory.make('Motor.go_ahead', ())

        '''中间传感器返回1走直线'''
        if status[0]['new'] == 0 and status[1]['new'] == 0 and status[2]['new'] == 1 and status[3]['new'] == 0 and status[4]['new'] == 0:
            return ActionFactory.make('Motor.go_ahead', ())

        '''31返回1左转'''
        if status[1]['new'] == 1:
            return ActionFactory.make('Motor.turn_left', ())

        '''35返回1右转'''
        if status[1]['new'] == 1:
            return ActionFactory.make('Motor.turn_right', ())
