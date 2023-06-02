from behavioral_patterns.command.command import Command

class ConcreteCommand1(Command):
    def execute(self):
        print("Executing Concrete Command 1...")