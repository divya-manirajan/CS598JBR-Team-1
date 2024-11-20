import java.lang.*;
import java.util.ArrayList;
import java.util.*;
import java.util.List;
import java.util.Collections;

class Solution {
    public static List<Integer> getOddCollatz(int n) {
        List<Integer> oddCollatz = new ArrayList<>();
        if (n % 2 == 1) {
            oddCollatz.add(n);
        }
        while (n > 1) {
            if (n % 2 == 0) {
                n = n / 2;
           			} else {
                n = n * 3 + 1;
            }
            if (n % 2 == 1) {
                oddCollatz.add(n);
            }
        }
        Collections.sort(oddCollatz);
        return oddCollatz;
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.getOddCollatz(14).equals(Arrays.asList(1, 5, 7, 11, 13, 17)),
                s.getOddCollatz(5).equals(Arrays.asList(1, 5)),
                s.getOddCollatz(12).equals(Arrays.asList(1, 3, 5)),
                s.getOddCollatz(1).equals(List.of(1))
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}