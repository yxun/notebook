package creational.abstract_factory;

public class USACarFactory {

    public static Car buildCar(CarType model) {
        Car car = null;
        switch (model) {
            case SMALL:
            car = new SmallCar(Location.USA);
            break;

            case SEDAN:
            car = new SedanCar(Location.USA);
            break;

            case LUXURY:
            car = new LuxuryCar(Location.USA);
            break;

            default:
            break;
        }
        return car;
    }
}