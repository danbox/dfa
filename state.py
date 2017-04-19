class State:

    transitions = {}

    def __init__(self, label, transitions):
        self.label = label

    def transition(self, symbol):
        return transitions[symbol]

