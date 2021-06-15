class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int[][] re = new int[r][c];
        int rows = mat.length;
        int colums = mat[0].length;
        if(r*c != rows*colums) return mat;

        int index = 0;
        for(int i=0; i<rows; i++){
            for(int j=0; j<colums; j++){
                re[index/c][index%c] = mat[i][j];       //分别除以c(列数),商和余数正好是所求
                index++;
            }
        }
        return re;
    }
}