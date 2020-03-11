package creational.prototype.factory;

import java.util.Map;
import java.util.HashMap;

import creational.prototype.contract.PrototypeCapable;
import creational.prototype.model.Album;
import creational.prototype.model.Movie;
import creational.prototype.model.Show;


public class PrototypeFactory {

    public static class ModelType {
        public static final String MOVIE = "movie";
        public static final String ALBUM = "album";
        public static final String SHOW = "show";
    }

    private static Map<String, PrototypeCapable> prototypes = new HashMap<String, PrototypeCapable>();

    static {
        prototypes.put(ModelType.MOVIE, new Movie());
        prototypes.put(ModelType.ALBUM, new Album());
        prototypes.put(ModelType.SHOW, new Show());
    }

    public static PrototypeCapable getInstance(final String s) throws CloneNotSupportedException {
        return ((PrototypeCapable) prototypes.get(s)).clone();
    }
}
