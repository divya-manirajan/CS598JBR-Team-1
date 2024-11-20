import java.lang.*;
import java.util.*;

class Solution {
    public static int fizzBuzz(int n) {
        StringBuilder ns = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                ns.append(i);
            }
        }
        String s = ns.toString();
        int ans = 0;
        for (char c : s.toCharArray()) {
            ans += (c == '7') ? 1 : 0;
        }
        return ans;
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.fizzBuzz(50) == 0,
                s.fizzBuzz(78) == 2,
                s.fizzBuzz(79) == 3,
                s.fizzBuzz(100) == 3,
                s.fizzBuzz(200) == 6,
                s.fizzBuzz(4000) == 192,
                s.fizzBuzz(10000) == 639,
                s.fizzBuzz(100000) == 8026
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}