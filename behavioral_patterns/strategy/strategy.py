class Strategy:
    def execute(self):
        raise NotImplementedError("Subclasses must implement execute method.")


class Strategy1(Strategy):
    def execute(self):
        print("Executing Strategy 1")


class Strategy2(Strategy):
    def execute(self):
        print("Executing Strategy 2")
