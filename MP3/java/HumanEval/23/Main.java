import java.lang.*;
import java.util.*;

class Solution {
public int strlen(String string) {
    /** Return length of given string
    System.out.println(strlen(""));
    0
    System.out.println(strlen("abc"));
    3
    */

    return string.length();
}

}
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Boolean> correct = Arrays.asList(
                s.strlen("") == 0,
                s.strlen("x") == 1,
                s.strlen("asdasnakj") == 9
        );
        if (correct.contains(false)) {
            throw new AssertionError();
        }
    }
}