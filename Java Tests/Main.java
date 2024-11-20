import java.util.*;
import java.util.Arrays;
import java.lang.*;
import java.util.stream.Collectors;
import java.util.List;

class Solution {
    public static List<String> wordsString(String s) { 
    // public static List<String> wordStrings(String s) { // correct method name
        if (s == null || s.isEmpty()) {
            return Arrays.asList();
        }

        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == ',') {
                sb.append(' ');
            } else {
                sb.append(c);
            }
        }

        return Arrays.stream(sb.toString().split(" "))
                // .filter(item -> !item.isEmpty()) // remove empty strings
                .collect(Collectors.toList());
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.wordStrings("Hi, my name is John" ).equals(Arrays.asList("Hi", "my", "name", "is", "John" )),
                s.wordStrings("One, two, three, four, five, six" ).equals(Arrays.asList("One", "two", "three", "four", "five", "six" )),
                s.wordStrings("Hi, my name" ).equals(Arrays.asList("Hi", "my", "name" )),
                s.wordStrings("One,, two, three, four, five, six," ).equals(Arrays.asList("One", "two", "three", "four", "five", "six" )),
                s.wordStrings("" ).equals(List.of()),
                s.wordStrings("ahmed     , gamal" ).equals(Arrays.asList("ahmed", "gamal" ))
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}
// [Hi, , my, name, is, John]
// [One, , two, , three, , four, , five, , six]
// [Hi, , my, name]
// [One, , , two, , three, , four, , five, , six]
// [ahmed, , , , , , , gamal]