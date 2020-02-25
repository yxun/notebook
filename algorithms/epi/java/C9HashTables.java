
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashSet;

public class C9HashTables {
    
    // Anagrams
    // two words are anagrams if and only if they result in equal strings after sorting
    // O(n^2mlongm), n is the number of strings and m is the maximum string length

    // the sorted strings are keys, and the values are arrays of the corresponding strings

    public static List<List<String>> findAnagrams(List<String> dictionary) {
        Map<String, List<String>> sortedStringToAnagrams = new HashMap<>();
        for (String s : dictionary) {
            char[] sortedCharArray = s.toCharArray();
            Arrays.sort(sortedCharArray);
            String sortedStr = new String(sortedCharArray);
            if (!sortedStringToAnagrams.containsKey(sortedStr)) {
                sortedStringToAnagrams.put(sortedStr, new ArrayList<String>());
            }
            sortedStringToAnagrams.get(sortedStr).add(s);
        }

        List<List<String>> anagramGroups = new ArrayList<>();
        for (Map.Entry<String, List<String>> p : sortedStringToAnagrams.entrySet()) {
            if (p.getValue().size() >= 2) {
                anagramGroups.add(p.getValue());
            }
        }
        return anagramGroups;
    }
    // O(nmlogm)

    // Design of a hashable class

    public static List<ContactList> mergeContactLists(List<ContactList> contacts) {
        return new ArrayList<>(new HashSet(contacts));
    }

    private static class ContactList {
        public List<String> names;

        ContactList(List<String> names) { this.names = names; }

        @Override
        public boolean equals(Object obj) {
            if (obj == null || !(obj instanceof ContactList)) {
                return false;
            }
            return this == obj ? true : new HashSet(names).equals(new HashSet(((ContactList)obj).names));
        }

        @Override
        public int hashCode() {
            return new HashSet(names).hashCode();
        }
    }


    // Know your hash table libraries
    // HashSet and HashMap, HashSet stores keys, HashMap stores key-value pairs
    // HashSet methods, add, remove, contains, iterator, isEmpty, size
    // both add and remove return a boolean indicating if the added/removed element was already present. null is a valid entry
    // The class LinkedHashSet subclasses HashSet, the only difference is that iterator() returns keys in the order in which they were inserted
    // HashSet retainAll(C) can be used to perform set intersection
    // HashMap methods, put, get, remove, containsKey
    // iteration, entrySet(), keySet(), values()
    // generic static inner class Map.Entry<K,V> is used to iterate over key-value pairs
    // to iterate in fixed order, use a LinkedHashMap

    // Is an anonymous letter constructible

    public static boolean isLetterConstructibleFromMagazine(String letterText, String magazineText) {
        Map<Character, Integer> charFrequencyForLetter = new HashMap<>();
        for (int i = 0; i < letterText.length(); i++) {
            char c = letterText.charAt(i);
            if (!charFrequencyForLetter.containsKey(c)) {
                charFrequencyForLetter.put(c, 1);
            } else {
                charFrequencyForLetter.put(c, charFrequencyForLetter.get(c) + 1);
            }
        }

        for (char c : magazineText.toCharArray()) {
            if (charFrequencyForLetter.containsKey(c)) {
                charFrequencyForLetter.put(c, charFrequencyForLetter.get(c) - 1);
                if (charFrequencyForLetter.get(c) == 0) {
                    charFrequencyForLetter.remove(c);
                    if (charFrequencyForLetter.isEmpty()) {
                        break;
                    }
                }
            }
        }
        return charFrequencyForLetter.isEmpty();
    }
    // time O(m+n)

}