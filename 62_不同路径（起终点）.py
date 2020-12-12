class Solution:
    def uniquePaths(self, m, n) :       #超时
        hang = n-1; lie = m-1              #行移动的次数，列移动的次数
        def unique(h,l):        #h,j表示还剩多少步可以走
            if h == 0 or l == 0:            #只有一种走法了
                return 1

            elif h > 0 and l > 0:           #不只一种走法
                return unique(h-1,l) + unique(h,l-1)            #向下走，或者向右走：：f(i,j)=f(i−1,j)+f(i,j−1)
        return unique(hang,lie)

class Solution1:                      #上边递归的优化-->动态规划
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]             #动态规划的表格
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]             #f(i,j)=f(i−1,j)+f(i,j−1)
        return f[m - 1][n - 1]

         #利用数学排列进行计算：：
        # 从左上角到右下角的过程中，我们需要移动 m+n-2m+n−2 次，
        # 其中有 m-1次向下移动，n-1次向右移动。因此路径的总数，
        # 就等于从 m+n-2次移动中选择 m-1 次向下移动的方案数
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


print(Solution1().uniquePaths(5,4))

