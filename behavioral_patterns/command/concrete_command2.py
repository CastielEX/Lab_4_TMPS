from behavioral_patterns.command.command import Command


class ConcreteCommand2(Command):
    def execute(self):
        print("Executing Concrete Command 2...")