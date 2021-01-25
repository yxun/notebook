package createObjects.hierarchicalbuilder;

import static createObjects.hierarchicalbuilder.NyPizza.Size.*;
import static createObjects.hierarchicalbuilder.Pizza.Topping.*;

// Using the hierarchical builder
public class PizzaTest {
    public static void main(String[] args) {
        NyPizza pizza = new NyPizza.Builder(SMALL)
            .addTopping(SAUSAGE).addTopping(ONION).build();
        Calzone calzone = new Calzone.Builder()
            .addTopping(HAM).sauceInside().build();

        System.out.println(pizza);
        System.out.println(calzone);
    }
}