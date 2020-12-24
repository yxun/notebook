package examples.singleton.enumtype;

// Enum singleton
public enum Elvis {
    INSTANCE;

    public void leaveTheBuilding() {
        System.out.println("I'm outta, here");
    }

    // This code would normally appear outside the class
    public static void main(String[] args) {
        Elvis elvis = Elvis.INSTANCE;
        elvis.leaveTheBuilding();
    }
}