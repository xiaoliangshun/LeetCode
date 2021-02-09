class Solution:                             #118. 杨辉三角 I  构造杨辉三角
    def generate(self, numRows: int):
        temp = []
        newtemp = []
        ans = []
        for i in range(1,numRows+1):            ##动态规划经常用是这样用前边运算的结果
            newtemp = [1]*i             #当前的行
            for j in range(1,i-1):      #第一个和最后一个不管
                newtemp[j] = temp[j-1] + temp[j]
            temp = newtemp[:]       #当前行变成上一行
            ans.append(newtemp)
        return ans

class Solution1:                         # 119. 杨辉三角 II   返回杨慧三角中的第k行(在上一个算法的基础上去掉ans)
    def getRow(self, rowIndex: int):
        temp = []
        newtemp = []
        for i in range(1, rowIndex + 2):  ##动态规划经常用是这样用前边运算的结果
            newtemp = [1] * i  # 当前的行
            for j in range(1, i - 1):  # 第一个和最后一个不管
                newtemp[j] = temp[j - 1] + temp[j]
            temp = newtemp[:]  # 当前行变成上一行
        return temp
    
print(Solution().generate(3))
print(Solution1().getRow(4))