import java.lang.*;
import java.util.*;

class Solution {
    public static boolean isMultiplyPrime(int a) {
        for (int i = 2; i <= 100; i++) {
            if (!isPrime(i)) continue;
            for (int j = 2; j <= 100; j++) {
                if (!isPrime(j)) continue;
                for (int k = 2; k <= 100; k++) {
                    if (!isPrime(k)) continue;
                    if (i * j * k == a) return true;
                }
            }
        }
        return false;
    }
    public static boolean isPrime(int n) {
        for (int j = 2; j < n; j++) {
            if (n % j == 0) return false;
        }
        return true;
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                !s.isMultiplyPrime(5),
                s.isMultiplyPrime(30),
                s.isMultiplyPrime(8),
                !s.isMultiplyPrime(10),
                s.isMultiplyPrime(125),
                s.isMultiplyPrime(3 * 5 * 7),
                !s.isMultiplyPrime(3 * 6 * 7),
                !s.isMultiplyPrime(9 * 9 * 9),
                !s.isMultiplyPrime(11 * 9 * 9),
                s.isMultiplyPrime(11 * 13 * 7)
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}