package creational.factory.car;

public class CarFactory {
    public static Car buildCar(CarType model) {
        Car car = null;
        switch (model) {
        case SMALL:
            car = new SmallCar();
            break;

        case SEDAN:
            car = new SedanCar();
            break;

        case LUXURY:
            car = new LuxuryCar();
            break;

        default:
            // throw some exception
            break;
        }
        return car;
    }
}

/** when to use factory pattern
 * The creation of an object prevents its reuse without significant duplication of code.
 * The creation of an object requires access to information or resources that should not be contained within the composing class.
 * The lifetime management of the generated objects must be centralized to ensure a consistent behavior within the application.
 */

/** Examples in JDK
 * java.sql.DriverMaanger#getConnection()
 * java.net.URL#openConnection()
 * java.lang.Class#newInstance()
 * java.lang.Class#forName()
 */
