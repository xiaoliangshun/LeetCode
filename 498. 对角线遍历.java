class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int row = mat.length;
        int colum = mat[0].length;
        int[] re = new int[row*colum];
        int index = 0;
        int x=0,y=0;    //表示开始的位置
        int[][] direct = {{-1,1},{1,-1}};       //表示右上和左下两个方向
        int d = 0;
        while(index < row*colum) {
            while (x > -1 && x < row && y < colum && y > -1) {      //合法
                re[index++] = mat[x][y];
                x += direct[d][0];
                y += direct[d][1];
            }
            if (x < 0 && y < colum) {               //在正上方溢出
                x += 1;         //拉回正轨
            } else if (x < 0 && y == colum) {              //在右上角
                x += 2;
                y -= 1;
            } else if (y > colum - 1) {        //在右方溢出
                x += 2;
                y -= 1;
            } else if (y < 0 && x < row) {              //在正左方溢出
                y += 1;
            } else if (x > row - 1) {          //在下方溢出
                x -= 1;
                y += 2;
            }

            if (d == 0) {             //转向
                d = 1;
            } else {
                d = 0;
            }
        }
        return re;
    }
}

        //可以考虑先对对角线迭代 ，然后进行翻转