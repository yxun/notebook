
# Collection

<<interface>> Collection 
- <<interface>> Set
- <<interface>> List
- <<interface>> Queue

<<interface>> Set
- <<interface>> SortedSet <-- TreeSet
- HashSet
- LinkedHashSet

<<interface>> List
- ArrayList
- Vector
- LinkedList

<<interface>> Queue
- LinkedList
- PriorityQueue

## Set

TreeSet, implememted by red-black tree. Used in searching from a range. O(logN)
HashSet, implemented by Hash Table. Used in quick search without order information
LinkedHashSet, implemented by Hash Table and double linked list to keep insertion order

## List

ArrayList, implemented by dynamic array, support random access
Vector, thread safe ArrayList
LinkedList, implemented by double linked list. Can be used in stack, queue or dequeue

## Queue

LinkedList, implemented by double linked list
PriorityQueue, implemented by heap

## Map

<<interface>> Map
- <<interface>> SortedMap <-- TreeMap
- HashTable
- LinkedHashMap
- HashMap

# Design Pattern

## Interator

Collection inherits Interable interface. Interable iterator() method produces an Interator object and Collection objects can use this method to iterate through elements.

From JDK 1.5+ we can use foreach method to implement Iterable interface object.

## Adapter

# JDK 8 Collection

## ArrayList

```java
public class ArrayList<E> extends AbstractList<E> 
    implements List<E>, RandomAccess, Cloneable, java.io.Serializable
```

Array default size is 10. 

```java
    private static final int DEFAULT_CAPACITY = 10;
```

### Grow capacity

```java
public boolean add(E e) {
    ensureCapacityInternal(size + 1);  // Increments modCount
    elementData[size++] = e;
    return true;
}

private void ensureCapacityInternal(int minCapacity) {
    if (elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA) {
        minCapaciy = Math.max(DEFAULT_CAPACITY, minCapacity);
    }
    ensureExplicitCapacity(minCapacity);
}

private void ensureExplicitCapacity(int minCapacity) {
    modCount++;
    // overflow-conscious code
    if (minCapacity - elementData.length > 0) {
        grow(minCapacity);
    }
}

private void grow(int minCapacity) {
    // overflow-conscious code
    int oldCapacity = elementData.length;
    int newCapacity = oldCapacity + (oldCapacity >> 1);
    if (newCapacity - minCapacity < 0)
        newCapacity = minCapacity;
    if (newCapacity - MAX_ARRAY_SIZE > 0)
        newCapacity = hugeCapacity(minCapacity);
    // minCapacity is usually close to size, so this is a win;
    elementdata = Arrays.copyOf(elementData, newCapacity);  // high performance cost step
}
```

### Delete element

Time O(N)

```java
public E remove(int index) {
    rangeCheck(index);
    modCount++;
    E oldValue = elementData(index);
    int numMoved = size - index - 1;
    if (numMoved > 0)
        System.arraycopy(elementData, index+1, elementData, index, numMoved);
    return oldValue;
}
```

### Serialization

Use keyword transient to avoid serializing the array. Use writeObject() and readObject() to serialize the non-empty part of the array.

```java
private void readObject(java.io.ObjectInputStream s) throws java.io.IOException, ClassNotFoundException {
    elementData = EMPTY_ELEMENTDATA;

    // Read in size, and any hidden stuff
    s.defaultReadObject();

    // Read in capacity
    s.readInt();  // ignored

    if (size > 0) {
        // be like  clone(), allocate array based upon size not capacity
        ensureCapacityInternal(size);

        Object[] a = elementData;
        // Read in all elements in the proper order
        for (int i = 0; i < size; i++) {
            a[i] = s.readObject();
        }
    }
}

private void writeObject(java.io.ObjectOutputStream s) throws java.io.IOException {
    // Write out element count, and any hidden stuff
    int expectedModCount = modCount;
    s.defaultWriteObject();

    // Write out size as capacity for behavioural compatibility with clone()
    s.writeInt(size);

    // Write out all elements in the proper order
    for (int i = 0; i < size; i++) {
        s.writeObject(elementData[i]);
    }

    if (modCount != expectedModCount) {
        throw new ConcurrentModificationException();
    }
}
```

## Vector

```java
public synchronized boolean add(E e) {
    modCount++;
    ensureCapacityHelper(elementCount+1);
    elementData[elementCount++] = e;
    return true;
}

public synchronized E get(int index) {
    if (index >= elementCount)
        throw new ArrayIndexOutOfBoundsException(index);
    return elementData(index);
}
```

### Grow capacity


