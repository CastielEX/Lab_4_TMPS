class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def perform_action(self):
        self.state.perform_action()