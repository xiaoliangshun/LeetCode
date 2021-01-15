class Solution:
    def restoreIpAddresses(self, s):
        temp = []
        ans = []
        def restore(s,temp):
            if len(temp) == 4:
                if len(s) == 0:
                    tt = ".".join(str(t) for t in temp)         ##将中间相邻的节点之间用.连接
                    ans.append(tt)
                return
            if s and int(s[0]) == 0:               ##为0时毫无疑问要单独当一位
                temp.append("0")
                restore(s[1:],temp)    #不用进行后续的循环了
                temp.pop()      ##也要回溯
                return
            for i in range(3):          ##最长就三位了
                if i < len(s):
                    if int(s[:i+1]) > 255:        ##此时不成立
                        return
                    else:
                        temp.append(s[:i+1])
                        restore(s[i+1:],temp)
                        temp.pop()              ##回溯
        restore(s,temp)
        return ans

s = "101023"
print(Solution().restoreIpAddresses(s))