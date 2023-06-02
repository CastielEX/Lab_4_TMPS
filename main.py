from behavioral_patterns.observer.subject import Subject
from behavioral_patterns.observer.observer import Observer

from behavioral_patterns.strategy import strategy1, strategy2
from behavioral_patterns import context

from behavioral_patterns.command.command import Command
from behavioral_patterns.command.concrete_command1 import ConcreteCommand1
from behavioral_patterns.command.concrete_command2 import ConcreteCommand2

from behavioral_patterns.state.context import Context as Context
from behavioral_patterns.state.state1 import State1
from behavioral_patterns.state.state2 import State2

if __name__ == "__main__":

    # Create instances of the strategies
    strategy1_instance = strategy1.Strategy1()
    strategy2_instance = strategy2.Strategy2()

    # Create contexts with the corresponding strategies
    context1 = context.Context(strategy1_instance)
    context2 = context.Context(strategy2_instance)

    # Execute the strategies
    context1.execute_strategy()
    context2.execute_strategy()


    # Observer Pattern
    subject = Subject()
    observer1 = Observer()
    observer2 = Observer()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("Message 1")

    subject.detach(observer1)

    subject.notify("Message 2")

    # Command Pattern
    command1 = ConcreteCommand1()
    command2 = ConcreteCommand2()

    command1.execute()
    command2.execute()

    # State Pattern
    state1 = State1()
    state2 = State2()

    context = Context()
    context.set_state(state1)
    context.perform_action()

    context.set_state(state2)
    context.perform_action()