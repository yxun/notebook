
## Data Types

### Primitive Types
- byte/8
- char/16
- short/16
- int/32
- float/32
- long/64
- double/64
- boolean/~

boolean has two values: true, false. can use 1 bit to store it. JVM compiles boolean type to int and use 1 to represent true, 0 is false. JVM supports boolean array, it uses byte array to represent it.

### Boxed Types

```java
Integer x = 2;      // autoboxing, calls Interger.valueOf(2)
int y = x;          // unboxing, calls X.intValue()
```

### Cache Pool

- new Integer(123) creates an instance for each call
- Integer.valueOf(123) uses the object in the cache. Each call uses a reference to the same object.

```java
Integer x = new Integer(123);
Integer y = new Integer(123);
System.out.println(x == y);  // false
Integer z = Integer.valueOf(123);
Integer k = Integer.valueOf(123);
System.out.println(z == k);  // true
```

```java
public static Integer valueOf(int i) {
    if (i >= IntegerCache.low && i <= IntegerCache.high)
        return IntegerCache.cache[i + (-IntegerCache.low)];
    return new Integer(i);
}
```

Java 8, Integer cache pool default size -128 ~ 127

```java
static final int low = -128;
static final int high;
static final Integer cache[];

static {
    // high value may be configured by property
    in h = 127;
    String integerCacheHighPropValue =
        sum.misc.VM.getSavedProperty("java.lang.Integer.IntegerCache.high");
    if (integerCacheHighPropValue != null) {
        try {
            int i = parseInt(integerCacheHighPropValue);
            i = Math.max(i, 127);
            // Maximum array size is Integer.MAX_VALUE
            h = Math.min(i, Integer.MAX_VALUE - (-low) - 1);
        } catch( NumberFormatException nfe ) {
            // If the property cannot be parsed into an int, ignore it.
        }
    }
    high = h;

    cache = new Integer[(hight - low) + 1];
    int j = low;
    for (int k = 0; k < cache.length; k++)
        cache[k] = new Integer(j++);
    // range [-128, 127] must be interned (JLS7 5.1.7)
    assert IntegerCache.high >= 127;
}
```

autoboxing uses valueOf() method

```java
Integer m = 123;
Integer n = 123;
System.out.println(m == n);  // true
```

primitive types cache:
- boolean values true and false
- all byte values
- short values between -128 and 127
- int values between -128 and 127
- char in the range \u0000 to \u007F

IntegerCache high default value is 127 but it can be configured. When jvm starts, -XX:AutoBoxCacheMax=<size> defines the size of the cache pool. It defines a system property java.lang.IntegerCache.high 

## String

Java 9

```java
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
        /** The value is used for character storage. */
        private final byte[] value;

        /** The identifier of the encoding used to encode the bytes in {@code value}. */
        private final byte coder;
    }
```

Advantage of immutable string

Use hash value for caching. For example using String as key in HashMap
String Pool
Security Safety
Thread Safety

### String, StringBuffer and StringBuilder

- String is immutable
- StringBuffer and StringBuilder are mutable

- String is thread safe
- StringBuilder is not thread safe
- StringBuffer is thread safe and it used synchronized internally.

### String Pool

String Pool stores literal strings. String method intern() can add a string into String Pool in runtime as well.

When using intern() method, if there is an equivalent string, String Pool returns the reference of the string. Otherwise, a new string is added in the String Pool and then return the reference.

literal string will be automatically added into String Pool.

```java
String s1 = new String("aaa");
String s2 = new String("aaa");
System.out.println(s1 == s2);       // false
String s3 = s1.intern();
String s4 = s1.intern();
System.out.println(s3 == s4);       // true

String s5 = "bbb";
String s6 = "bbb";
System.out.println(s5 == s6);       // true
```

new String("abc") creates two string objects if the literal string is not in the String Pool.
The value array is pointing to the same array.

```java
public String(String original) {
    this.value = original.value;
    this.hash = original.hash;
}
```

## Operation

### method parameters
Java is using copy-by-value for parsing parameters in a method. If a parameter is a reference, it copies the referece to the same object.

```java


public class PassByValueExample {
    public static void main(String[] args) {
        Dog dog = new Dog("A");
        System.out.println(dog.getObjectAddress());  // Dog@455617c
        func(dog);
        System.out.println(dog.getObjectAddress());  // Dog@455617c
        System.out.println(dog.getName());           // A
    }
}

private static void func(Dog dog) {
    System.out.println(dog.getObjectAddress());  // Dog@455617c
    dog = new Dog("B");
    System.out.println(dog.getObjectAddress());  // Dog@74a144
    System.out.println(dog.getName());           // B
}

class Dog {
    String name;

    Dog(String name) {
        this.name = name;
    }

    String getName() {
        return this.name;
    }

    void setName(String name) {
        this.name = name;
    }

    String getObjectAddress() {
        return super.toString();
    }
}
```

### compound operators casting

s1 += 1;  // short s1
s1++

equals to s1 = (short) (s1 + 1)

### switch

switch condition statement with String
```java
String s = "a";
switch (s) {
    case "a":
        System.out.println("aaa");
        break;
    case "b":
        System.out.println("bbb");
        break;
}
```

cannot use long in condition statement. supported types: 'char, byte, short, int, Character, Byte, Short, Integer, String, or an enum'

## Built-in Keywords

### final

1. data

- primitive type, final makes the value consistent.
- referece type, final makes the referece value consistent, but the referenced object may still be able to be modified.

2. method

final method cannot be overloaded by child classes. 
private method is also a final method. If there is a child class method which has the same signature with a parent class method, the child class method does not overload the parent one. It defines a new method in the child class.

3. class

final class cannot be inherited.

### static

1. data

A static field is a class field. All instances share the same static field.

```java
public class A {

    private int x;          // instance field
    private static int y;   // static field

    public static void main(String[] args) {
        // int x = A.x;  // Non-static field 'x' cannot be referenced from a static context
        A a = new A();
        int x = a.x;
        int y = A.y;
    }
}
```

2. method

A static method does not need a class instance. So a static method must be a concrete method and it cannot be an abstract method. It is illegal combination of modifiers: 'abstract' and 'static'.

A static method can not include keyword 'this' or 'super'. Those two keywords must be associated with an instance.

```java
public class A {

    private static int x;
    private int y;

    public static void func1() {
        int a = x;
        // int b = y; // Non-static field 'y' cannot be referenced from a static context
        // int b = this.y;  // 'A.this' cannot be referenced from a static context
    }
}
```

3. statement

static statement(s) will be executed when a class is loaded.

```java
public class A {
    static {
        System.out.println("123");
    }

    public static void main(String[] args) {
        A a1 = new A();
        A a2 = new A();
    }
}

// print 123 once

```

4. inner class

Non-static inner class instantiation needs an instance of the outer class. Static inner class don't need that.

```java
public class OuterClass {

    class InnerClass {}

    static class StaticInnerClass {}

    public static void main(String[] args) {
        // InnerClass innerClass = new InnerClass();  // 'OuterClass.this' cannot be referenced from a static context
        OuterClass outerClass = new OuterClass();
        InnerClass innerClass = outerClass.new InnerClass();
        StaticInnerClass staticInnerClass = new StaticInnerClass();
    }
}
```

static inner class cannot visit non-static fields or methods in the outer class.

5. import package

```java
import static com.xxx.ClassName.*
```

when using static fields or method, we don't need to mention ClassName.

6. initialization order

- parent class (static fields, static statements)
- child class (static fieds, static statements)
- parent class (non-static fields, non-static statements)
- parent class constructor
- child class (non-static fields, non-static statements)
- child class constructor


## Object common methods

Overview

```java
public native int hashCode()

public boolean equals(Object obj)

protected native Object clone() throws CloneNotSupportedException

public String toString()

public final native Class<?> getClass()

protected void finalize() throws Throwable {}

public final native void notify()

public final native void notifyAll()

public final native void wait(long timeout) throws InterruptedException

public final void wait(long timeout, int nanos) throws InterruptedException

public final void wait() throws InterruptedException

```

### equals()

Five conditions of equality:
- x.equals(x);  // true, self reflection
- x.equals(y) == y.equals(x);   // true symetric
- if (x.equals(y) && y.equals(z)) x.equals(z); // true 
- x.equals(y) == x.equals(y);   // true consistent result when calling multiple times
- x.equals(null);   // false, when x is not a null object

When comparing primitive types, use == , there is no equals() method in primitive types
When comparing reference typess, == compares if two variables are referencing the same object (reference value); equals() compares if the referenced objects are equivalent.

```java
Integer x = new Integer(1);
Integer y = new Integer(1);
System.out.println(x.equals(y));    // true
System.out.println(x == y);         // false
```

Implementation details:
- If two references refer to the same object, return true
- If two objects are not the same types, return false
- Type assertion of the Object object
- Compare each field of the object

For example,

```java
public class EqualExample {

    private int x;
    private int y;
    private int z;

    public EqualExample(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        EqualExample that = (EqualExample) o;

        if (x != that.x) return false;
        if (y != that.y) return false;
        return z == that.z;
    }
}
```

### hashCode()

when two objects are equivalent, their hash values are same. However, when two objects have same hash value, they may not be equivalent.

When override equals() method, user should also override hashCode() method. And make sure two equivalent objects have same hash value.

