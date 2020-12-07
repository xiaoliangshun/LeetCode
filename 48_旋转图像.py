class Solution1:                                 #学会利用已有工具，而不是从最原始的方式求解---》效率更高
    def rotate(self, matrix):                   #########--------先转置矩阵，然后翻转每一行
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):                   #转置
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

                # reverse each row
        for i in range(n):
            matrix[i].reverse()                  #每一行都倒置---->相当于每一列都倒置

class Solution:
    def rotate(self, matrix):            #先存四个待旋转的值，再进行旋转放入
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row            #先存4个待旋转的值
                # rotate 4 elements
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]         #放回
                    row, col = col, n - 1 - row

class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]                                 #直接旋转
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

nums = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(Solution().rotate(nums))

