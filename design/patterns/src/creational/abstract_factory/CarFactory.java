package creational.abstract_factory;

public class CarFactory {

    private CarFactory() {
        //Prevent instantiation
    }

    public static Car buildCar(CarType type) {
        Car car = null;
        Location location = Location.ASIA;  // Read location property somewhere
        // Use location specific car factory
        switch(location) {
            case USA:
            car = USACarFactory.buildCar(type);
            break;

            case ASIA:
            car = AsiaCarFactory.buildCar(type);
            break;

            default:
            car = DefaultCarFactory.buildCar(type);
        }
        return car;
    }
}