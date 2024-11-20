import java.lang.*;
import java.util.*;

class Solution {
    public static boolean isNested(String string) {
        List<Integer> openingBracketIndex = new ArrayList<>();
        List<Integer> closingBracketIndex = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            if (string.charAt(i) == '[') {
                openingBracketIndex.add(i);
            } else {
                closingBracketIndex.add(i);
           }
        }
        closingBracketIndex.sort(Comparator.reverseOrder());
        int cnt = 0;
        int i = 0;
        int l = closingBracketIndex.size();
        for (int idx : openingBracketIndex) {
            if (i < l && idx < closingBracketIndex.get(i)) {
                cnt += 1;
                i += 1;
            }
        }
        return cnt >= 2;
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.isNested("[[]]" ),
                !s.isNested("[]]]]]]][[[[[]" ),
                !s.isNested("[][]" ),
                !s.isNested("[]" ),
                s.isNested("[[[[]]]]" ),
                !s.isNested("[]]]]]]]]]]" ),
                s.isNested("[][][[]]" ),
                !s.isNested("[[]" ),
                !s.isNested("[]]" ),
                s.isNested("[[]][[" ),
                s.isNested("[[][]]" ),
                !s.isNested("" ),
                !s.isNested("[[[[[[[[" ),
                !s.isNested("]]]]]]]]" )
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}