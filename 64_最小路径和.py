class Solution:

            #与“62题”一样的动态规划，我们可以从左上角开始计算其下和右边的路径距离，
            #比较元素的上方和左边的路径那个距离小，就选择他+该元素 作为该元素的最短距离
    def minPathSum(self, grid) :
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]       #for _ in range(rows)：表示循环rows次
        dp[0][0] = grid[0][0]
        for i in range(1, rows):                #初始化行
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):             #初始化列
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]

   # 链接：https: // leetcode - cn.com / problems / minimum - path - sum / solution / zui - xiao - lu - jing - he - by - leetcode - solution /

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))

