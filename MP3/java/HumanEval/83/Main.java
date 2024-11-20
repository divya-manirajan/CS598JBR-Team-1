import java.lang.*;
import java.util.*;

class Solution {
    public static int startsOneEnds(int n) {
        /**
         * Given a positive integer n, return the count of the numbers of n-digit
         * positive integers that start or end with 1.
         */

        if (n == 1) return 1;
        return 18 * (int) Math.pow(10, n - 2);
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.startsOneEnds(1) == 1,
                s.startsOneEnds(2) == 18,
                s.startsOneEnds(3) == 180,
                s.startsOneEnds(4) == 1800,
                s.startsOneEnds(5) == 18000
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}