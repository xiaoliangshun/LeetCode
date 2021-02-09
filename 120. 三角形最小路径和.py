class Solution:
    def minimumTotal(self, triangle):
        def mini(row,col,count):      #row表示行数，col表示改行的第几个,count表示累积的和         超时了
            global countMax
            if (row == leng and count < countMax):      #到达叶子节点
                countMax = count
                return
            for i in range(2):
                if row < leng and col <= row:
                    # print(row,col,count)
                    mini(row+1,col+i,count+triangle[row][col])

        leng = len(triangle)
        if leng == 1:
            return triangle[0][0]
        global countMax
        countMax = 88888
        mini(0,0,0)
        return countMax

    ###法2：：：：；动态规划法
    状态转移方程为：
    # f[i][i]表示从顶点到i行j列的最短路径
    # 状态转移方程：
    # f[i][j] = min(f[i−1][j−1], f[i−1][j])+c[i][j]
    class Solution:
        def minimumTotal(self, triangle: List[List[int]]) -> int:
            n = len(triangle)
            f = [[0] * n for _ in range(n)]             ##for _ in range(n)中_ 是占位符， 表示不在意变量的值 只是用于循环遍历n次。  这里表示构造等腰三角数组
            f[0][0] = triangle[0][0]

            for i in range(1, n):
                f[i][0] = f[i - 1][0] + triangle[i][0]      #特殊情况：上一行的左边没有了（只能从正上方过来）
                for j in range(1, i):
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
                f[i][i] = f[i - 1][i - 1] + triangle[i][i]          #特殊情况：正上方的那个没有（不能从正上方过来）

            return min(f[n - 1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle1 = [[10]]
print(Solution().minimumTotal(triangle))