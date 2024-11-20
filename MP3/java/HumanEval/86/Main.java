import java.util.*;
import java.lang.*;
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public static String antiShuffle(String s) {
        return Arrays.stream(s.split(" "))
                .map(word -> word.chars()
                        .sorted()
                        .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                        .toString())
                .collect(Collectors.joining(" "));
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                Objects.equals(s.antiShuffle("Hi"), "Hi"),
                Objects.equals(s.antiShuffle("hello"), "ehllo"),
                Objects.equals(s.antiShuffle("number"), "bemnru"),
                Objects.equals(s.antiShuffle("abcd"), "abcd"),
                Objects.equals(s.antiShuffle("Hello World!!!"), "Hello !!!Wdlor"),
                Objects.equals(s.antiShuffle(""), ""),
                Objects.equals(s.antiShuffle("Hi. My name is Mister Robot. How are you?"), ".Hi My aemn is Meirst .Rboot How aer ?ouy")
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}