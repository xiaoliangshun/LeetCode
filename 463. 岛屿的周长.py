class Solution:
    ## 迭代
    def islandPerimeter(self, grid):
        row,col = len(grid),len(grid[0])            #行数和列数
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        leng = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num = 4
                    for r,c in direct:              # 向四个方向走
                        if i+r != -1 and i+r != row and j+c != -1 and j+c != col:      # 边缘
                            if grid[i+r][j+c] == 1:           # 有邻居
                                num -= 1
                    leng += num
        return leng

    ## 深度优先遍历
    # 三种状态：0：水   1：陆地   2：已访问
# class Solution {
#         static int[] dx = {0, 1, 0, -1};
#         static int[] dy = {1, 0, -1, 0};
#
#         public int islandPerimeter(int[][] grid) {
#             int n = grid.length, m = grid[0].length;
#             int ans = 0;
#             for (int i = 0; i < n; ++i) {
#                 for (int j = 0; j < m; ++j) {
#                     if (grid[i][j] == 1) {
#                         ans += dfs(i, j, grid, n, m);
#                         }
#                 }
#              }
#     return ans;
#     }
#
#     public int dfs(int x, int y, int[][] grid, int n, int m) {
#         if (x < 0 | | x >= n | | y < 0 | | y >= m | | grid[x][y] == 0) {
#             return 1;                                     #到边了或没有陆地了
#         }
#     if (grid[x][y] == 2) {                ##标记的已经访问了
#         return 0;
#         }
#     grid[x][y] = 2;           #标记
#     int res = 0;
#     for (int i = 0; i < 4; ++i){      #往四个面找
#         int tx = x + dx[i];
#         int ty = y + dy[i];
#         res += dfs(tx, ty, grid, n, m);
#         }
#     return res;
#     }
# }


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))