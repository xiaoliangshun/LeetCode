class Solution:
    def wordBreak(self, s, wordDict):              #超时
        def word(s,wordDict):
            if len(s) == 0:
                return True

            for w in wordDict:                      #试着匹配每一个单词
                if w == s[:len(w)]:
                    if word(s[len(w):],wordDict):           #剩余的继续匹配
                        return True                     #有一个匹配成功就ok
            return False
        return word(s,wordDict)

    ####  动态规划法
    ##转移方程：
    # dp[i] = dp[j] && check(s[j..i−1])
    #     dp[i] 表示字符串 s前 i 个字符组成的字符串s[0..i−1] 是否能被空格拆分成若干个字典中出现的单词
    # 其中 check(s[j..i−1]) 表示子串s[j..i−1] 是否出现在字典中。
    def wordBreak2(self, s, wordDict):
        # public class Solution {              ##java代码
        #     public boolean wordBreak(String s, List < String > wordDict) {
        #         Set < String > wordDictSet = new HashSet(wordDict);
        #         boolean[] dp = new boolean[s.length() + 1];
        #         dp[0] = true;
        #         for (int i = 1; i <= s.length(); i++) {
        #           for (int j = 0; j < i; j++) {
        #               if (dp[j] && wordDictSet.contains(s.substring(j, i))) {     #后边的j~i也要成立才行
        #                   dp[i] = true;
        #                   break;
        #               }
        #           }
        #         }
        # return dp[s.length()];
        #   }
        # }
    def wordBreak2(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[len(s)]


    #想法：可以把字典表中的元素变成树，前缀相等的在一样的祖父上，给每一个节点标记一个额外的指针，如果是字典中单词到了结尾，则将该指针指向头节点，意味着重新开始
        ##如果哪一步不匹配直接分会False，否则True
s = "leetcode"
sword = ["leet","code"]
print(Solution().wordBreak2(s,sword))
