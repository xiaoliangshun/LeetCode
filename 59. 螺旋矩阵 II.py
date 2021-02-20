class Solution:
    def generateMatrix(self, n):            #59. 螺旋矩阵II 与54.螺旋矩阵   使用的方法相同
        ####方法一：模拟(确定四个方向，遍历)

        visited = [[False] * n for _ in range(n)]          ##记录是否遍历的数组
        order = [[0] * n for _ in range(n)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]             #四个方向
        row, column = 0, 0         #当前位置
        directionIndex = 0      #当前方向
        for i in range(n**2):
            order[row][column] = i+1
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < n and 0 <= nextColumn < n and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4               #调转方向
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order

print(Solution().generateMatrix(3))