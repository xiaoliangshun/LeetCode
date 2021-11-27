import java.util.LinkedList;

class Solution {        //法1:从1开始找最近的0
    int[] dx = {0,0,1,-1};
    int[] dy = {1,-1,0,0};
    public int[][] updateMatrix(int[][] mat) {      //超时
        //广度优先遍历
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                if(mat[i][j]==1) mat[i][j] = updateXY(mat,i,j);
            }
        }
        return mat;
    }
    public int updateXY(int[][] mat, int x, int y){
        boolean[][] visied = new boolean[mat.length][mat[0].length];        //其实也可以不使用访问数组，在原数组上+[最大数+1]，就可以复原
        LinkedList<Point> queue = new LinkedList<>();
        queue.offer(new Point(x,y));
        int deep = 1;      //深度
        while (!queue.isEmpty()){
            int size = queue.size();        //记录栈里边元素的个数[上层节点的个数]
            for (int j = 0; j < size; j++) {
                Point p = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nextX = p.x1+dx[i];
                    int nextY = p.y1+dy[i];
                    if(nextX>=0 && nextY>=0 && nextX<mat.length && nextY<mat[0].length && !visied[nextX][nextY]){
                        if(mat[nextX][nextY]==0){
                            return deep;
                        }else{
                            queue.offer(new Point(nextX,nextY));
                            visied[nextX][nextY]=true;      //设为已访问
                        }
                    }
                }
            }
            deep++;     //深度+1
        }
        return deep;
    }
}
class Point{
    int x1;
    int y1;
    public Point(){}
    public Point(int x1, int y1) {
        this.x1 = x1;
        this.y1 = y1;
    }
}

class Solution1 {           //中心扩散[广度优先]
//    从0开始向四周扩散
    static int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] dist = new int[m][n];
        boolean[][] seen = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<int[]>();
        // 将所有的 0 添加进初始队列中
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                    seen[i][j] = true;
                }
            }
        }

        // 广度优先搜索
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int i = cell[0], j = cell[1];
            for (int d = 0; d < 4; ++d) {
                int ni = i + dirs[d][0];
                int nj = j + dirs[d][1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && !seen[ni][nj]) {
                    dist[ni][nj] = dist[i][j] + 1;
                    queue.offer(new int[]{ni, nj});
                    seen[ni][nj] = true;
                }
            }
        }
        return dist;
    }
}