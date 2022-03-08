public class Solution {
    public int addDigits(int num) {
        int n = num;
        return  n - 9 * ((n-1)/9);
    }
}