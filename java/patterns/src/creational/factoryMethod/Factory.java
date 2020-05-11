package creational.factoryMethod;

public abstract class Factory {

    abstract public Product factoryMethod();
    public void doSomething() {
        Product product = factoryMethod();
        // do something
    }
}
