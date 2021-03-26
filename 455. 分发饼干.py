class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ## s能满足，i，j都后移      （遍历s）
        # s不能满足，i不动，j后移找到能满足的

        g.sort(reverse=True)        #从大到小排
        s.sort(reverse=True)
        count = 0
        i,j = 0,0
        while i < len(s):         #提供者从大到小来试试
            if s[i] >= g[j]:       #可以满足，就看下一个
                i += 1
                count += 1
            if j < len(g)-1:        #g必须还在元素
                j += 1   
            else:
                return count       
        return count