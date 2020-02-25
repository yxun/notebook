
import java.util.Comparator;
import java.util.List;
import java.util.Collections;

public class C8Searching {

    // Binary search
    public static int bsearch(int t, List<Integer> A) {
        int L = 0, U = A.size()-1;
        while (L <= U) {
            int M = L + (U-L)/2;
            if (A.get(M) < t) {
                L = M + 1;
            } else if (A.get(M) == t) {
                return M;
            } else {
                U = M - 1;
            }
        }
        return -1;
    }
    // time T(n) = T(n/2) + c, O(logn)

    // Searching boot camp
    private static class Student {
        public String name;
        public double gradePointAverage;

        Student(String name, double gradePointAverage) {
            this.name = name;
            this.gradePointAverage = gradePointAverage;
        }
    }

    private static final Comparator<Student> compGPA = new Comparator<Student>() {
        @Override
        public int compare(Student a, Student b) {
            if (a.gradePointAverage != b.gradePointAverage) {
                return Double.compare(a.gradePointAverage, b.gradePointAverage);
            }
            return a.name.compareTo(b.name);
        }
    };

    public static boolean searchStudent(List<Student> students, Student target, Comparator<Student> compGPA) {
        return Collections.binarySearch(students, target, compGPA) >= 0;
    }
    // time O(logn)

    // Know your searching libraries
    // Arrays.binarySearch(A, "a")
    // Collections.binarySearch(list, 42)
    // If the search key is not present, both methods return (-(insertion point)-1),
    // where insertion point is defined as the point at which the key would be inserted into the array

    // Search a sorted array for first occurrence of k

    public static int searchFirstOfK(List<Integer> A, int k) {
        int left = 0, right = A.size()-1, result = -1;
        while (left <= right) {
            int mid = left + ((right - left) / 2);
            if (A.get(mid) > k) {
                right = mid - 1;
            } else if (A.get(mid) == k) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }
}