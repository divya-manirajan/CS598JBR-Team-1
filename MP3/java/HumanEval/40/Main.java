import java.lang.*;
import java.util.List;
import java.util.*;

class Solution {
    public static boolean triplesSumToZero(List<Integer> list) {
        for (int i = 0; i < list.size(); i++) {
            for (int j = i + 1; j < list.size(); j++) {
                for (int k = j + 1; k < list.size(); k++) {
                    if (list.get(i) + list.get(j) + list.get(k) == 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(1, 3, 5, 0))),
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(1, 3, 5, -1))),
                s.triplesSumToZero(new ArrayList<>(Arrays.asList(1, 3, -2, 1))),
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(1, 2, 3, 7))),
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(1, 2, 5, 7))),
                s.triplesSumToZero(new ArrayList<>(Arrays.asList(2, 4, -5, 3, 9, 7))),
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(1))),
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(1, 3, 5, -100))),
                !s.triplesSumToZero(new ArrayList<>(Arrays.asList(100, 3, 5, -100)))
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}