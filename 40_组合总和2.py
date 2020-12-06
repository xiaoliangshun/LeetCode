class Solution:
    def combinationSum2(self, candidates, target):
        def combin(candidates,target,list2):
            if target == 0:
                list1.append(list2)
                return
            else:                              #可以试试的  >0时
                for cand in candidates:
                    sub = target - cand
                    if sub == 0:
                        combin(candidates,sub,list2+[cand])
                    elif sub < 0:                         #不用继续了，后边更大
                        return
                    else:                            #试试
                        candidates_copy = candidates.copy()
                        candidates_copy.remove(cand)               #下次不用他了
                        combin(candidates_copy,sub,list2+[cand])               #+[元素]可以，-[元素]不可以
        def repeat():             #去重不到位
            i = 0
            while i < len(list1):
                s1 = set(list1[i])
                i += 1
                j = i
                while j < len(list1):
                    s2 = set(list1[j])
                    if s1 == s2:
                        list1.pop(j)
                    j += 1
            return list1
        list1 = list()
        list2 = list()
        candidates.sort()
        combin(candidates,8,list2)
        repeat()

        return list1                   #再去重




# 相同的数放在一起进行处理，也就是说，如果数x 出现了y 次，那么在递归时一次性地处理它们，即分别调用选择 0,1,⋯,y 次x 的递归函数。这样我们就不会得到重复的组合。
# 我们用dfs(pos,rest) 表示递归的函数，其中 pos 表示我们当前递归到了数组candidates 中的第 pos 个数，而 rest 表示我们还需要选择和为rest 的数放入列表作为一个组合；
#
# 对于当前的第pos 个数，我们有两种方法：选或者不选。如果我们选了这个数，那么我们调用dfs(pos+1,rest−candidates[pos]) 进行递归，注意这里必须满足rest≥candidates[pos]。如果我们不选这个数，那么我们调用dfs(pos+1,rest) 进行递归；
#
# 在某次递归开始前，如果rest 的值为 00，说明我们找到了一个和为 target 的组合，将其放入答案中。
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]       #将后边的most个数去掉      #[::-1]  表示逆转      [::-2] 从后往前一次走两部     [:-n] 开始到导数第n个数

        freq = sorted(collections.Counter(candidates).items())             #freq[元素][0] 该元素  freq[元素][1]  元素频率
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans

nums = [10,1,2,7,6,1,5]
print(Solution().combinationSum2(nums,8))

