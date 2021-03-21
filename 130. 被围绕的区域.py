class Solution:
    def solve(self, board: List[List[str]]) -> None:            #深度优先：从四周开始，将是O的元素向四个方向走
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':          #只遍历是O的元素，且是没有被遍历过的
                return

            board[x][y] = "A"       #相当于标记，标记完后下次就不能访问了
            dfs(x + 1, y)           ##朝上下左右四个可以去的方向走
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):      ##最外围开始
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):      ##外围开始
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":      ##标记为A的就是通过外围能做到的地方
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def solve2(self, board: List[List[str]]) -> None:           ##广度优先，从外围一圈一圈走
        if not board:
            return

        n, m = len(board), len(board[0])
        que = collections.deque()
        for i in range(n):              #最外围的O进入队列
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
        for i in range(m - 1):
            if board[0][i] == "O":
                que.append((0, i))
            if board[n - 1][i] == "O":
                que.append((n - 1, i))

        while que:
            x, y = que.popleft()
            board[x][y] = "A"           ##已经走过的O
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:     #找四个方向
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"