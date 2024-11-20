import java.lang.*;
import java.util.ArrayList;
import java.util.List;
import java.util.*;

class Solution {
    public static List<Integer> makeAPile(int n) {
        List<Integer> pile = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            pile.add(n + 2 * i);
        }
        return pile;
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.makeAPile(3).equals(Arrays.asList(3, 5, 7)),
                s.makeAPile(4).equals(Arrays.asList(4, 6, 8, 10)),
                s.makeAPile(5).equals(Arrays.asList(5, 7, 9, 11, 13)),
                s.makeAPile(6).equals(Arrays.asList(6, 8, 10, 12, 14, 16)),
                s.makeAPile(8).equals(Arrays.asList(8, 10, 12, 14, 16, 18, 20, 22))
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}