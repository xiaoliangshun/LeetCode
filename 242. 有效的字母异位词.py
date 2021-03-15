class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False
        for i in range(lenT):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1
        for i in range(lenT):
            if t[i] in dict1 and dict1[t[i]] >= 1:
                dict1[t[i]] -= 1
            else:
                return False
        return True

    ##法2 排序  将s和t排序后从前到后比较


s = "rat"
t = "car"
print(Solution().isAnagram(s, t))