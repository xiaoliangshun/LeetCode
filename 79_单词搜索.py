import collections
class Solution:
    def exist(self, board, word) :                      #有问题？？？？？？
        ans = collections.defaultdict(list)    #------------------------设置字典value中的类型（这里是数组）
        for i in range(len(board)):
            for j in range(len(board[i])):
                ans[board[i][j]].append([i,j])
        print(ans)
        listFlag = [[[0]*len(board[0])]*len(board)]
        print(listFlag)
        def existword(i,j,a):
            if listFlag[i][j] != 0 and board[i][j] == a:    #没有走过而且刚好匹配
                return True
            else:
                return False
        def existmain(i,j,k):
            if word[k] not in ans:
                return False
            else:
                if existword(i,j,word[k]):
                    return existmain(i,j+1,word[k+1]) or existmain(i,j-1,word[k+1]) \
                           or existmain(i+1,j,word[k+1]) or existmain(i-1,j,word[k+1])      #没有处理回溯时，将标记数组设空

        for i, j in ans[word[0]]:
            if existmain(i,j,0):
                return True
        return False

class Solution1:                    #leetcode答案
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]             #四个方向走

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True                                 #成功出口

            visited.add((i, j))                         #标记不一定要用数组，，set()集合也不错，不用存储大量元素
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))                  #很关键（走不通，换条道）
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False
链接：https: // leetcode - cn.com / problems / word - search / solution / dan - ci - sou - suo - by - leetcode - solution /

board =[      ['A','B','C','E'],
                ['S','F','C','S'],
                    ['A','D','E','E']
        ]

print(Solution().exist(board,"AB"))

