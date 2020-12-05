class Solution:
    def combinationSum(self, candidates,target):               #-------------我的代码。。？？有问题
        list1 = []            #成立的结果
        list2 = []              #试试的结果
        def combination(candidates,target,list1,list2):
            for index in range(len(candidates)):
                if target-candidates[index] > 0:
                    combination(candidates,target-candidates[index],list1,list2+[candidates[index]])    #添加时注意在外边加[]
                elif target-candidates[index] == 0:
                    list2.append(candidates[index])
                    list1.append(list2)
                    return
                else:
                    break
        candidates.sort()
        combination(candidates,target,list1,list2)
        print(list1)
        i = 0
        while i < len(list1)-1:             #去重(不充分)
            set1 = set(list1[i])
            set2 = set(list1[i+1])
            if set1 == set2:
                del list1[i+1]            #删除元素：根据索引：del list[index]  .pop(index)[默认善最后一个]   根据值：.remove(value)  .clear()全部删除
                i -= 1
            i += 1
        return list1
num = [3,5,8]
print(Solution().combinationSum(num,11))
from typing import List


    def combinationSum2(self, candidates:, target):        ##------参考-------！！与金条切割一样(不同的是每次切割我们要存储所有上午切割方案而不是最有利益的方案)

    def dfs(candidates, begin, size, path, res, target):
        if target == 0:
            res.append(path)
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            if residue < 0:              #已经排好序了，后边就更不可能了
                break

            dfs(candidates, index, size, path + [candidates[index]], res, residue)   #>=0时，可以尝试,,这里的begin=index才是去重复的关键，这样的排序使得最终的输出结果是非递减的序列

    size = len(candidates)
    if size == 0:
        return []
    candidates.sort()      #排序后（减去当前值后，如果小于0，就不用再继续了）
    path = []                #试试
    res = []                  #最终的结果（全局变量）
    dfs(candidates, 0, size, path, res, target)
    return res
