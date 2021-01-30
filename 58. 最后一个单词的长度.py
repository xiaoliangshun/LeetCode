class Solution:
    def lengthOfLastWord(self, s: str) -> int:      #题目要求从左到右    如果是从后往前遍历就太简单了
        count = 0
        lastCount = 0
        flag = False       ##判断是不是第一个空格
        i = 0
        leng = len(s)
        while i < leng:
            if s[i] == " ":
                if flag == False:       #第一个空格
                    lastCount = count           #将本次的count存一下，防止最后是几个空格count清零
                    flag = True     #表示再往后的空格就不是第一个了
                count = 0
            else:
                flag = False        #刷新
                count += 1
            i += 1
        if count == 0 and lastCount != 0:
            return lastCount
        return count

print(Solution().lengthOfLastWord("a  "))
