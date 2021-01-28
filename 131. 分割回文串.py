class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(List,tmp):
            if not List:
                res.append(tmp)
                return
            for i in range(len(List)):          #一棵树
                if List[:i+1]==List[i::-1]:         #回文判断
                    backtrack(List[i+1:],tmp+[List[:i+1]])          ##这里不用撤销的原因：就是传入的参数是调整后的，回来后就还原了
        backtrack(s,[])
        return res



class Solution:                                                         ##########我的写法：有问题
    def partition(self, s: str) -> List[List[str]]:
        def parttt(start, end):  ##判断回文
            while (start <= end):
                if s[start] != s[end]:
                    return False
            return True

        def part(start, end):  # 两边都是闭区间
            for i in range(end - start + 1):
                if not parttt(start, start + i):
                    continue
                ans.append(s[start:start + i])  ##加入
                part(start + 1, end)
                ans.remove()  # 回溯

        ans = []
        part(0, len(s) - 1)
        return ans
s = "101023"
print(Solution().restoreIpAddresses(s))