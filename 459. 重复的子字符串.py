class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        leng = len(s)
        for i in range(1, leng):        #查找符合的
            if s[i] == s[0]:        ##匹配s[0:i-1]与后边的情况
                if leng % i == 0:           #剩余的位置够整数倍
                    for n in range(1,leng // i):
                        if s[:i] != s[i*n : i*n+i]:         #切片前闭后开[a,b)
                            break
                        if n == leng // i - 1 and s[:i] == s[i*n : 2*i+n]:
                            return True                    # 最后一次匹配成功
        return False
print(Solution().repeatedSubstringPattern("ababababab"))


    # 遍历
    def repeatedSubstringPattern2(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):      # 看所有的差距为i的值是否相等
                    return True
        return False

    ##匹配  判断是否具有若干相同成分：可以将两个拼接后，将齿轮往后挪一个，查找能否吻合
    def repeatedSubstringPattern3(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)                 ##两个s拼接之后，从ss中第二个元素开始找是否存在s，（返回的是在ss中匹配的下标）
                ## 假设s是由多个s'组成，其实就是将s往后错了一位，这样的话其实就是在检查每一个s'与下一个s'是否相等，相等的话s中就含有n个s'

    ## KMP算法