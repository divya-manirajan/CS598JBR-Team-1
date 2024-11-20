import java.lang.*;
import java.util.HashSet;
import java.util.Set;
import java.util.*;
import java.util.Arrays;

class Solution {
    public static boolean sameChars(String s0, String s1) {
        Set<Character> set0 = new HashSet<>();
        Set<Character> set1 = new HashSet<>();

        for (char c : s0.toCharArray()) {
            set0.add(c);
        }

        for (char c : s1.toCharArray()) {
            set1.add(c);
        }

        return set0.equals(set1);
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.sameChars("eabcdzzzz", "dddzzzzzzzddeddabc"),
                s.sameChars("abcd", "dddddddabc"),
                s.sameChars("dddddddabc", "abcd"),
                !s.sameChars("eabcd", "dddddddabc"),
                !s.sameChars("abcd", "dddddddabcf"),
                !s.sameChars("eabcdzzzz", "dddzzzzzzzddddabc"),
                !s.sameChars("aabb", "aaccc")
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}