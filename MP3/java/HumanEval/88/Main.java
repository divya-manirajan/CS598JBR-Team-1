import java.lang.*;
import java.util.Arrays;
import java.util.*;

class Solution {
    public static void sortArray(int[] array) {
        if (array.length == 0) {
            return;
        }
        Arrays.sort(array);
        if ((array[0] + array[array.length - 1]) % 2 == 0) {
            reverseArray(array);
        }
    }
    public static void reverseArray(int[] array) {
        for (int i = 0; i < array.length / 2; i++) {
            int temp = array[i];
            array[i] = array[array.length - 1 - i];
            array[array.length - 1 - i] = temp;
        }
    }

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.sortArray(new ArrayList<>(List.of())).equals(List.of()),
                s.sortArray(new ArrayList<>(List.of(5))).equals(List.of(5)),
                s.sortArray(new ArrayList<>(Arrays.asList(2, 4, 3, 0, 1, 5))).equals(Arrays.asList(0, 1, 2, 3, 4, 5)),
                s.sortArray(new ArrayList<>(Arrays.asList(2, 4, 3, 0, 1, 5, 6))).equals(Arrays.asList(6, 5, 4, 3, 2, 1, 0)),
                s.sortArray(new ArrayList<>(Arrays.asList(2, 1))).equals(Arrays.asList(1, 2)),
                s.sortArray(new ArrayList<>(Arrays.asList(15, 42, 87, 32 ,11, 0))).equals(Arrays.asList(0, 11, 15, 32, 42, 87)),
                s.sortArray(new ArrayList<>(Arrays.asList(21, 14, 23, 11))).equals(Arrays.asList(23, 21, 14, 11))
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}