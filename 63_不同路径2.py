class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        import numpy as np
        row, col = len(obstacleGrid), len(obstacleGrid[0])  # 行数和列数
        # list1 = [[0]*col]*row               ##这种方法生成的矩阵是[0]*col的row个复制品，一个变其余的row个位置也跟着变
        list1 = np.zeros([row, col], dtype=int)             # 使用numpy的矩阵（m*n,初始为0的矩阵）
        for i in range(col):        # 行初始化          可以在下边遍历的时候处理，从时间上看，是一样的
            if obstacleGrid[0][i] == 1:
                break           # 遇见一个障碍物后边的就都不能到了，默认为0，不应管
            else:
                list1[0][i] = 1
        for i in range(row):            # 列初始化
            if obstacleGrid[i][0] == 1:
                break
            else:
                list1[i][0] = 1
        for i in range(1, row):  # 跳过第一行
            for j in range(1, col):  # 跳过第一列
                if obstacleGrid[i][j] == 0:  # 非障碍物       障碍物默认为0，不处理
                    list1[i][j] = list1[i - 1][j] + list1[i][j - 1]
        return int(list1[row - 1][col - 1])

nums = [[0,0],[1,0],[1,0]]
print(Solution().uniquePathsWithObstacles(nums))


nums1 = [0]*5               ##这种方法生成的矩阵是[0]*col的row个复制品，一个变其余的row个位置也跟着变
nums1[2] = 1
print(nums1)