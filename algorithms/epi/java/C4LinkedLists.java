
class ListNode<T> {
    public T data;
    public ListNode<T> next;
    
}

public class C4LinkedLists {

    // Linked lists boot camp

    public static ListNode<Integer> search(ListNode<Integer> L, int key) {
        while (L != null && L.data != key) {
            L = L.next;
        }

        return L;
    }

    // Insert newNode after node
    public static void insertAfter(ListNode<Integer> node, ListNode<Integer> newNode) {
        newNode.next = node.next;
        node.next = newNode;
    }

    // Delete the node immediately following aNode. Assumes aNode is not a tail.
    public static void deleteList(ListNode<Integer> aNode) {
        aNode.next = aNode.next.next;
    }

    // Consider using a dummy head to avoid having to check for empty lists
    // It's easy to forget to update next for the head and tail.
    // Benefit from using two iterators, one ahead of the other, or one advancing quicker than the other

    // Know your linked list libraries
    // The two most commonly used implementations of the List interface are ArrayList (dynamically resized array) and LinkedList (doubly linked list)

    // Useful methods in Collections class:
    // Collections.addAll(C, 1,2,4), Collections.binarySearch(list, 42),
    // Collections.fill(list, 'f'), Collections.swap(C, 0, 1),
    // Collections.min(C), Collections.min(C,cmp), Collections.max(C)
    // Collections.reverse(list), Collections.rotate(list, 12),
    // Collections.sort(list), Collections.sort(list, cmp)

    // Arrays.asList() you can efficiently create tuples
    // The object returned by Arrays.asList(array), is partially mutable: you can change existing entries, but you cannot add or delete entries.
    // Arrays.asList() on an array of primitive type, e.g. Arrays.asList(new int[]1,2,4), you will get a list with a single entry, [1,2,4]
    // Arrays.asList(new Integer[]1,2,4)
    // To preserve the original array, make a copy of it, e.g., Arrays.copyOf(A, A.length)

    // Test for cyclicity
    // In each iteration, advance the slow iterator by one and the fast iterator by two

    public static ListNode<Integer> hasCycle(ListNode<Integer> head) {
        ListNode<Integer> fast = head, slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                // There is a cycle, so now let's calculate the cycle length
                int cycleLen = 0;
                do {
                    ++cycleLen;
                    fast = fast.next;
                } while (slow != fast);

                // Finds the start of the cycle
                ListNode<Integer> cycleLenAdvancedIter = head;
                // cycleLenAdvancedIter pointer advances cycleLen first
                while (cycleLen-- > 0) {
                    cycleLenAdvancedIter = cycleLenAdvancedIter.next;
                }

                ListNode<Integer> iter = head;
                // Both iterators advance in tandem
                while (iter != cycleLenAdvancedIter) {
                    iter = iter.next;
                    cycleLenAdvancedIter = cycleLenAdvancedIter.next;
                }
                return iter;  // iter is the start of cycle
            }
        }
        return null;  // no cycle
    }
}
