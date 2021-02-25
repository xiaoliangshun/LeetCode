class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def isIs(s,t):
            leng = len(s)
            dict1 = dict()          #使用字典（哈希表）记忆映射关系
            for i in range(leng):
                if s[i] in dict1 and  dict1[s[i]] != t[i]:
                    return False
                else:
                    dict1[s[i]] = t[i]
            return True
        return isIs(s,t) and isIs(t,s)          ##相同字符只能映射到同一个字符上，反过来再算一遍就是：不同字符不能映射到同一个字符上

    ##方法2：可以将s数组排序，t也按照s的排序顺序重组
    ##此时应当是s中相同的元素连在一起，对比s中从前到后连续的个数，与t对比，不相同则返回False，若s中不相同元素的个数与t中不相同的元素个数不同，返回False
    
s = "add"
t = "add"
print(Solution().isIsomorphic(s,t))