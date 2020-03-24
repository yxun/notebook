
Bridge design pattern is used to decouple a class into two parts - abstraction and it's implementation - so that both can evolve in future without affecting each other. It increases the loose coupling between class abstraction and it's implementation.

You get this decoupling by adding one more redirection between methods calls from abstraction to implementation.

Participants:
- Abstraction (abstract class): It defined the abstract interface i.e. behavior part. It also maintains the Implementer reference.
- RefinedAbstraction (normal class): It extends the interface defined by Abstraction.
- Implementer (interface): It defines the interface for implementation classes. This interface does not need to correspoind directly to abstraction interface and can be very different. Abstraction imp provides an implementation in terms of operations provided by Implementer interface.
- ConcreteImplementor (normal class): It implements the Implementer interface.

The Bridge pattern is an application of the old advice, "prefer composition over inheritance". It becomes handy when you must subclass different times in ways that are orthogonal with one another.

Bridge design pattern is most applicable in applications where you need to provide platform independence.

Notes:
- Bridge pattern decouple an abstraction from its implementation so that the two can very independently.
- It is used mainly for implementing platform independence feature.
- It adds one more method level redirection to achieve the objective.
- Publish abstraction interface in separate inheritance hierarchy, and put implementation in its own inheritance hierarchy,
- Use bridge pattern to run-time binding of the implementation.
- Use bridge pattern to map orthogonal class hierachies.
- Bridge is designed up-front to let the abstraction and the implementation very independently.


