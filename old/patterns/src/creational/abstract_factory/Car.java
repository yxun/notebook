package creational.abstract_factory;

public abstract class Car {
    protected abstract void construct();

    private CarType model = null;
    private Location location = null;
    
    public Car(CarType model, Location location) {
        this.model = model;
        this.location = location;
    }

    // getters and setters

    @Override
    public String toString() {
        return "Model-" + model + " built in " + location;
    }
}
