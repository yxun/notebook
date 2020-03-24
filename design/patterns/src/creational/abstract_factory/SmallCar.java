package creational.abstract_factory;

public class SmallCar extends Car {

    public SmallCar(Location location) {
        super(CarType.SMALL, location);
        construct();
    }

    @Override
    protected void construct() {
        System.out.println("Building small car");
    }
}
