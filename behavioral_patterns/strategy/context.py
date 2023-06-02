class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()
