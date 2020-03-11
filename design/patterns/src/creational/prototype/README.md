
Prototype design pattern is used in scenarios where application needs to create a large number of instances of a class, which have almost same state or differ very little.

An instance of actual object (i.e. prototype) is created on starting, and thereafter whenever a new instance is required, this prototype is cloned to have another instance.
If deep copy is needed, you can use memory serialization.

Pattern Participants
- Prototype
- Prototype registry: have all prototypes accessible using simple string parameters
- Client: use registry service to access prototype instances


