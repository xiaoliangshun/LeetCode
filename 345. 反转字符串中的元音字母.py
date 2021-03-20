class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lst = list(s)        #变成数组了
        ###3333Python 3中字符串不可被改变，如果使用str.replace方法改变字符串，则原字符串不变，新建一个改变后的字符串。

        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if lst[l] in dic and lst[r] in dic:
                lst[l], lst[r] = lst[r], lst[l]
                l = l + 1
                r = r - 1
            elif lst[l] not in dic:
                l = l + 1
            elif lst[r] not in dic:
                r = r - 1

        return ''.join(lst)         #将lst连接起来，且中间不加任何东西


