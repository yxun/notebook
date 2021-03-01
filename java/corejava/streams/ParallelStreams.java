package streams;

import java.io.IOException;
import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.Map;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;

public class ParallelStreams {
    public static void main(String[] args) throws IOException {
        String contents = new String(Files.readAllBytes(
            Paths.get("alice30.txt")), StandardCharsets.UTF_8);
        List<String> wordList = Arrays.asList(contents.split("\\PL+"));

        // Remedy: Group and count
        Map<Integer, Long> shortWordCounts = wordList.parallelStream()
            .filter(s -> s.length() < 10)
            .collect(Collectors.groupingBy(String::length, Collectors.counting()));
            
        System.out.println(shortWordCounts);

        // Downstream order not deterministic
        Map<Integer, List<String>> result = wordList.parallelStream()
            .collect(
                Collectors.groupingByConcurrent(String::length)
            );
        System.out.println(result.get(14));

        result = wordList.parallelStream().collect(
            Collectors.groupingByConcurrent(String::length)
        );

        System.out.println(result.get(14));

        Map<Integer, Long> wordCounts = wordList.parallelStream()
            .collect(
                Collectors.groupingByConcurrent(String::length, Collectors.counting())
            );
        System.out.println(wordCounts);
    }
}
