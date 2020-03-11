package creational.builder.user;

// Builder pattern aims to 
// “Separate the construction of a complex object from its representation 
// so that the same construction process can create different representations.”

public class User {

    // All final attributes
    private final String firstName; // required
    private final String lastName;  // required
    private final int age;          // optional
    private final String phone;     // optional
    private final String address;   // optional

    private User(UserBuilder builder) {
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.age = builder.age;
        this.phone = builder.phone;
        this.address = builder.address;
    }

    // All getter, and No setter to provide immutability
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }
    
    public int getAge() {
        return age;
    }

    public String getPhone() {
        return phone;
    }

    public String getAddress() {
        return address;
    }

    @Override
    public String toString() {
        return "User: " +
                this.firstName + ", " +
                this.lastName + ", " +
                this.age + ", " +
                this.phone + "," +
                this.address;
    }


    public static class UserBuilder {
        private final String firstName;
        private final String lastName;
        private int age;
        private String phone;
        private String address;

        public UserBuilder(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public UserBuilder age(int age) {
            this.age = age;
            return this;
        }

        public UserBuilder phone(String phone) {
            this.phone = phone;
            return this;
        }

        public UserBuilder address(String address) {
            this.address = address;
            return this;
        }

        // Return the finally constructed User object
        public User build() {
            User user = new User(this);
            validateUserObject(user);
            return user;
        }

        private void validateUserObject(User user) {
            // Do some basic validations to check
            // if user object does not break any assumption

        }
    }

    public static void main(String[] args) {
        User user1 = new User.UserBuilder("Lokesh", "Gupta")
            .age(30)
            .phone("123456")
            .address("fake address 123")
            .build();
        System.out.println(user1);

        User user2 = new User.UserBuilder("Jack", "Reacher")
            .age(40)
            .phone("2345")
            // no address
            .build();
        System.out.println(user2);

        User user3 = new User.UserBuilder("Super", "Man")
            .build();
        System.out.println(user3);

    }

    /** Existing implementations in JDK
     * java.lang.StringBuilder#append()
     * java.lang.StringBuffer#append()
     * java.nio.ByteBuffer#put()
     * javax.swing.GroupLayout.Group#addComponent()
     */

    /** Advantages
     * design flexibility
     * more readable code
     * reduced parameters to the constructor
     * highly readable method calls
     * no need to pass in null for optional parameters
     * help build immutable objects
     */

    /** Disadvantages
     * double up total lines of code
     * client is more verbose
     */

    /** References
     * http://en.wikipedia.org/wiki/Builder_pattern
     * http://www.javaspecialists.eu/archive/Issue163.html
     * http://en.wikipedia.org/wiki/Fluent_interface
     * http://martinfowler.com/bliki/FluentInterface.html
     */

}



