
import java.util.List;
import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;

public class C10Sorting {

    // Sorting boot camp

    private static class Student implements Comparable<Student> {
        public String name;
        public double gradePointAverage;

        public int compareTo(Student that) { return name.compareTo(that.name); }

        Student(String name, double gradePointAverage) {
            this.name = name;
            this.gradePointAverage = gradePointAverage;
        }
    }

    public static void sortByName(List<Student> students) {
        Collections.sort(students);
    }

    public static void sortByGPA(List<Student> students) {
        Collections.sort(
            students, Collections.reverseOrder(new Comparator<Student>() {
                @Override
                public int compare(Student a, Student b) {
                    return Double.compare(a.gradePointAverage, b.gradePointAverage);
                }
            })
        );
    }
    
    // Know your sorting libraries
    // To sort an array, use Arrays.sort(A), and to sort a list use Collections.sort(list)
    // Arrays.sort(A), Collections.sort(A) operates on arrays of objects that implement the Comparable interface  

    // use sorting to make the subsequent steps in an algorithm simpler
    // design a custom sorting routine

    // Compute the intersection of two sorted arrays
    // brute-force time O(mn)

    // iterate through the first array and use binary search in array to test if the element is present in the second array
    // time O(mlogn), it's a good solution if one set is much smaller than the other.
    public static List<Integer> intersectTwoSortedArrays(List<Integer> A, List<Integer> B) {
        List<Integer> intersectionAB = new ArrayList<>();
        for (int i = 0; i < A.size(); ++i) {
            if (( i == 0 || A.get(i) != A.get(i-1)) && Collections.binarySearch(B, A.get(i)) >= 0) {
                intersectionAB.add(A.get(i));
            }
        }
        return intersectionAB;
    }

    // simultaneously advancing through the two input arrays in increasing order
    // time O(m+n)
    public static List<Integer> intersectTwoSortedArrays2(List<Integer> A, List<Integer> B) {
        List<Integer> intersectionAB = new ArrayList<>();
        int i = 0, j = 0;
        while (i < A.size() && j < B.size()) {
            if (A.get(i) == B.get(j) && (i == 0 || A.get(i) != A.get(i-1))) {
                intersectionAB.add(A.get(i));
                ++i;
                ++j;
            } else if (A.get(i) < B.get(j)) {
                ++i;
            } else {  // A.get(i) > B.get(j)
                ++j;
            }
        }
        return intersectionAB;
    }

    // Render a calendar, takes a set of events, and determines the maximum number of events that take place concurrently
    private static class Event {
        public int start, finish;

        public Event(int start, int finish) {
            this.start = start;
            this.finish = finish;
        }
    }

    private static class Endpoint implements Comparable<Endpoint> {
        public int time;
        public boolean isStart;

        public int compareTo(Endpoint e) {
            if (time != e.time) {
                return Integer.compare(time, e.time);
            }
            // If times are equal, an endpoint that starts an interval comes first
            return isStart && !e.isStart ? -1 : !isStart && e.isStart ? 1 : 0;
        }

        Endpoint(int t, boolean is) {
            time = t;
            isStart = is;
        }
    }

    public static int findMaxSimultaneousEvents(List<Event> A) {
        // Builds an array of all endpoints
        List<Endpoint> E = new ArrayList<>();
        for (Event event : A) {
            E.add(new Endpoint(event.start, true));
            E.add(new Endpoint(event.finish, false));
        }
        // Sorts the endpoint array according to the time, breaking ties
        // by putting start times before end times
        Collections.sort(E);

        // Track the number of simultaneous events, and record the maximum
        // number of simultaneous events
        int maxNumSimultaneousEvents = 0, numSimultaneousEvents = 0;
        for (Endpoint endpoint : E) {
            if (endpoint.isStart) {
                ++numSimultaneousEvents;
                maxNumSimultaneousEvents = Math.max(numSimultaneousEvents, maxNumSimultaneousEvents);
            } else {
                --numSimultaneousEvents;
            }
        }
        return maxNumSimultaneousEvents;
    }
    // time O(nlogn), space O(n)
}