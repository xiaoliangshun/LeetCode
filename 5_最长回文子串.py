class Solution:
    def longestPalindrome(self, s: str) -> str:     ######我的：应该可以实现
        import numpy as np
        leng = len(s)
        if leng == 0:
            return 0
        elif leng == 1:
            return 1
        else:
            list1 = np.ones(leng,dtype=int)                #list[i] = j 表示第i个元素的前j个元素是回文（包含自己）
            if s[1] == s[0]:
                list1[1] = 2
            for i in range(2,leng):
                if s[i] == s[i-list1[i-1]-1]:               #比较该元素与上一个元素的前边没有匹配的值比较
                    list1[i] = list1[i-1] + 2
                elif s[i] == s[i-1]:
                    list1[i] = list1[i-1]+1
        return max(list1)

# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
    ####暴力解法。。。
    ####马拉车算法（Manacher）   ？？？？？？
    ####中心扩散法
    # 状态转移方程：
    # P(i, i) = true
    # P(i, i + 1) =(Si == Si+1)
    # P(i + 1, j - 1)=P(i+1,j-1)and(Si == Sj)

    class Solution:
        def expandAroundCenter(self, s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        def longestPalindrome(self, s: str) -> str:
            start, end = 0, 0
            for i in range(len(s)):
                left1, right1 = self.expandAroundCenter(s, i, i)
                left2, right2 = self.expandAroundCenter(s, i, i + 1)
                if right1 - left1 > end - start:
                    start, end = left1, right1
                if right2 - left2 > end - start:
                    start, end = left2, right2
            return s[start: end + 1]

    ####动态规划法
        ##状态转移方程：
        # P(i,j)=P(i+1,j−1)∧(Si ==Sj)
        # 动态规划的边界条件：
        # P(i, i) =  {true}
        # P(i, i + 1) = (Si == S(i+1))
    class Solution:
        def longestPalindrome(self, s: str) -> str:
            n = len(s)
            dp = [[False] * n for _ in range(n)]            #二维转移方程表
            ans = ""
            # 枚举子串的长度 l+1
            for l in range(n):
                # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
                for i in range(n):
                    j = i + l
                    if j >= len(s):
                        break
                    if l == 0:
                        dp[i][j] = True
                    elif l == 1:
                        dp[i][j] = (s[i] == s[j])
                    else:
                        dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                    if dp[i][j] and l + 1 > len(ans):
                        ans = s[i:j + 1]
            return ans

s = "cbbd"
print(Solution().longestPalindrome(s))

