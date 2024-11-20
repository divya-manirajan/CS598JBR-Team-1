import java.lang.*;
import java.util.*;

class Solution {
    public static int fib4(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be >= 0");
        }

        int[] results = {0, 0, 2, 0};
        if (n < 4) {
            return results[n];
        }

        for (int i = 4; i <= n; i++) {
            int newResult = results[3] + results[2] + results[1] + results[0];
            System.arraycopy(results, 0, results, 1, 3);
            results[0] = newResult;
        }

        return results[0];
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.fib4(5) == 4,
                s.fib4(8) == 28,
                s.fib4(10) == 104,
                s.fib4(12) == 386
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}