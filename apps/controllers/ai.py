import json


class AI:
    def __init__(self):
        self.actionStream = {}
        self.load_action()

    def store_action(self):
        with open('actionstream.json', 'w') as f:
            f.write(json.dumps(self.actionStream))

    def load_action(self):
        with open('actionstream.json', 'r') as f:
            self.actionStream = json.loads(f.read())
