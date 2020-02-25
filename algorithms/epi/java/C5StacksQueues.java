
import java.util.Deque;
import java.util.LinkedList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.ArrayList;

public class C5StacksQueues {

    public static class ListNode<T> {
        public T data;
        public ListNode<T> next;
    }

    // Stacks boot camp
    // useful for creating reverse interators for sequences
    // time and space O(n)
    public static void printLinkedListInReverse(ListNode<Integer> head) {
        Deque<Integer> nodes = new LinkedList<>();
        while (head != null) {
            nodes.addFirst(head.data);
            head = head.next;
        }
        while (!nodes.isEmpty()) {
            System.out.println(nodes.poll());
        }
    }

    // Know your stack libraries
    // The preferred way to represent stacks in Java is via the Deque interface
    // The LinkedList class is a doubly linked list that implements this interface
    // The key methods in the Deque are: push(42), peek(), pop(), isEmpty()
    // Other useful methods: descendingIterator(), iterator()

    // Implement a stack with MAX API
    // for each entry in the stack, we cache the maximum stored at or below that entry

    private static class ElementWithCachedMax {
        public Integer element;
        public Integer max;

        public ElementWithCachedMax(Integer element, Integer max) {
            this.element = element;
            this.max = max;
        }
    }

    static class Stack {
        // Stores (element, cached maximum) pair
        private Deque<ElementWithCachedMax> elementWithCachedMax = new LinkedList<>();

        public boolean empty() { 
            return elementWithCachedMax.isEmpty(); 
        }

        public Integer max() {
            if (empty()) {
                throw new IllegalStateException("max(): empty stack");
            }
            return elementWithCachedMax.peek().max;
        }

        public Integer pop() {
            if (empty()) {
                throw new IllegalStateException("pop(): empty stack");
            }
            return elementWithCachedMax.removeFirst().element;
        }

        public void push(Integer x) {
            elementWithCachedMax.addFirst(
                new ElementWithCachedMax(x, Math.max(x, empty() ? x : max()))
            );
        }
    }
    // Each methods time O(1), space O(n)


    // Queues boot camp
    // use composition: add a private field that references a library queue object and forward existing methods

    class QueueWithMaxIntro {
        private Deque<Integer> data = new LinkedList<>();

        public void enqueue(Integer x) {
            data.add(x);
        }

        public Integer dequeue() {
            return data.removeFirst();
        }

        public Integer max() {
            if (!data.isEmpty()) {
                return Collections.max(data);
            }
            throw new IllegalStateException("cannot perform max() on empty queue");
        }
    }

    // Compute binary tree nodes in order of increasing depth
    // use a queue of nodes to store nodes at depth i and a queue of nodes at depth i+1

    class BinaryTreeNode<T> {
        public T data;
        public BinaryTreeNode<T> left, right;
    }

    public static List<List<Integer>> binaryTreeDepthOrder( BinaryTreeNode<Integer> tree) {
        Queue<BinaryTreeNode<Integer>> currDepthNodes = new LinkedList<>();
        currDepthNodes.add(tree);
        List<List<Integer>> result = new ArrayList<>();

        while (!currDepthNodes.isEmpty()) {
            Queue<BinaryTreeNode<Integer>> nextDepthNodes = new LinkedList<>();
            List<Integer> thisLevel = new ArrayList<>();
            while (!currDepthNodes.isEmpty()) {
                BinaryTreeNode<Integer> curr = currDepthNodes.poll();
                if (curr != null) {
                    thisLevel.add(curr.data);

                    // Defer the null checks to the null test above
                    nextDepthNodes.add(curr.left);
                    nextDepthNodes.add(curr.right);
                }
            }

            if (!thisLevel.isEmpty()) {
                result.add(thisLevel);
            }
            currDepthNodes = nextDepthNodes;
        }
        return result;
    }
    // time O(n), space O(m) where m is the maximum number of nodes at any single depth
    
}
