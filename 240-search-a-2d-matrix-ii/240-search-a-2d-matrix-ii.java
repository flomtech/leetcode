class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int t = target;
         
        if(matrix == null || matrix.length == 0){
            return false;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int i = (m - 1);
        int j = 0;
        while( i >= 0 && j < n){
            int cur = matrix[i][j];
            if(cur == t){
                return true;
            }else if(t > cur){
                j++;
            }else{
                i--;
            }
        }
        return false;
    }
}