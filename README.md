# Lab_4_TMPS

Observer Pattern:

1. The Subject class represents a subject that maintains a list of observers and allows observers to subscribe (attach) and unsubscribe (detach) to it.
The Observer class defines an abstract observer that needs to be implemented by concrete observer classes.
When the state of the subject changes, it notifies all subscribed observers by invoking their update method.
Strategy Pattern:

2. The Context class represents a context that uses a strategy.
The Strategy1 and Strategy2 classes are concrete strategies that encapsulate different algorithms.
The context can be configured with a specific strategy using the set_strategy method, and the execute_strategy method executes the strategy.
Command Pattern:

3. The Command class defines an abstract command that needs to be implemented by concrete command classes.
The ConcreteCommand1 and ConcreteCommand2 classes are concrete commands that encapsulate different actions.
The commands can be executed by invoking their execute method.
State Pattern:

4. The Context class represents a context that can change its behavior based on its internal state.
The State1 and State2 classes are concrete states that encapsulate different behaviors.
The context can be configured with a specific state using the set_state method, and the perform_action method performs an action based on the current state.
