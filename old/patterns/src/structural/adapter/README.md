Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

A adapter pattern is also known as a Wrapper pattern. The main use of this pattern is when a class that you need to use doesn't meet the requirements of an interface.

Participants of Adapter Design Pattern
- Target: It defines the application-specific interface that Client uses directly
- Adapter: It adapts the interface Adaptee to the Target interface. It's middle man
- Adaptee: It defines an existing incompatible interface that needs adapting before using in application
- Client: It is your application that works with Target interface


