
import java.util.List;
import java.util.Iterator;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.ArrayList;


public class C7Heaps {

    // max-heap, the key at each node is at least as great as the keys stored at its children
    // a max-heap can be implemented as an array, the children of the node at index i are at indices 2i+1 and 2i+2
    // a max-heap supports O(logn) insertions, O(1) lookup for the max element, and O(logn) deletion of the max element

    // Heaps boot camp
    // keep k longest strings, min-heap

    public static List<String> topK(int k, Iterator<String> iter) {
        PriorityQueue<String> minHeap = new PriorityQueue<>(k, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return Integer.compare(s1.length(), s2.length());
            }
        });
        while (iter.hasNext()) {
            minHeap.add(iter.next());
            if (minHeap.size() > k) {
                // Remove the shortest string
                // The comparison function above will order the strings by length
                minHeap.poll();
            }
        }
        return new ArrayList<>(minHeap);
    }
    // process time O(nlogk)

    // Know heap libraries
    // PriorityQueue, key methods add(), peek(), poll()

    // Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence

    private static class ArrayEntry {
        public Integer value;
        public Integer arrayId;

        public ArrayEntry(Integer value, Integer arrayId) {
            this.value = value;
            this.arrayId = arrayId;
        }
    }

    public static List<Integer> mergeSortedArrays(List<List<Integer>> sortedArrays) {
        List<Iterator<Integer>> iters = new ArrayList<>(sortedArrays.size());
        for (List<Integer> array : sortedArrays) {
            iters.add(array.iterator());
        }
        PriorityQueue<ArrayEntry> minHeap = new PriorityQueue<>(
            (int)sortedArrays.size(), new Comparator<ArrayEntry>() {
                @Override
                public int compare(ArrayEntry o1, ArrayEntry o2) {
                    return Integer.compare(o1.value, o2.value);
                }
            }
        );
        for (int i = 0; i < iters.size(); ++i) {
            if (iters.get(i).hasNext()) {
                minHeap.add(new ArrayEntry(iters.get(i).next(), i));
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!minHeap.isEmpty()) {
            ArrayEntry headEntry = minHeap.poll();
            result.add(headEntry.value);
            if (iters.get(headEntry.arrayId).hasNext()) {
                minHeap.add(new ArrayEntry(iters.get(headEntry.arrayId).next(), headEntry.arrayId));
            }
        }
        return result;
    }
    // time O(nlogk), space O(k)
}