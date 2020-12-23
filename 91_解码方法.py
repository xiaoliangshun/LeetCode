class Solution:
    def numDecodings(self, s):
        if s[0] == "0":
            return 0
        count = 1
        pre = 1
        for i in range(1,len(s)):
            temp = count
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":          #当前元素为0，必须与前边组成10/20才有意义，s[i]与s[i-1]就必须绑定在一起
                    count = pre
                else:
                    return 0
            elif s[i-1] == "1" or (s[i-1] == "2" and 1 <= int(s[i]) <= 6):      #可以去前边的值相连形成一个新的，也可以不连
                count += pre                                                        #还有一种就是3~9开头的，无论加什么都不能跟前边的匹配，解码方法不变
            pre = temp              #记录上此的值
        return count


print(Solution().numDecodings("01"))
