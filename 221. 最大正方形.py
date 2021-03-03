class Solution:

    #方法一：暴力法
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):                ##以每一个点作为正方形的左上角，寻找最大正方形
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)        #右下方有多少位置
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':             #判断右下角位置
                            break
                        for m in range(k):                              #判断新增的下边一行和右边一列
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:                #右下全为1
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare

        #方法二：动态规划
        # dp(i,j)表示以第i，j个为右下角时，左上方的最大正方形
        # 如果该位置的值0，则dp(i,j) = 0
        # 如果该位置的值是1，则dp(i, j)的值由其上方、左方和左上方的三个相邻位置的值决定。具体而言，当前位置的元素值等于三个相邻位置的元素中的最小值加1，状态转移方程如下：
        # dp(i, j) = min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]           #动态规划数组
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:            ##第一行和第一列
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare


matri =  [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(matri))


