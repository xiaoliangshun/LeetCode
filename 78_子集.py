class Solution:
    def subsets(self, nums):
        list1 = list()
        list2 = list()
        leng = len(nums)
        flag = True
        def sub(nums,l):
            if l == leng:
                list2_copy = list2.copy()
                list1.append(list2_copy)
            if l < leng:
                list2.append(nums[l])           #放进来（一遍）
                sub(nums,l+1)
                list2.remove(nums[l])              #移除去（又一遍）
                sub(nums,l+1)
        sub(nums,0)
        return list1
    
grid = [1,2,3]
print(Solution().subsets(grid))

