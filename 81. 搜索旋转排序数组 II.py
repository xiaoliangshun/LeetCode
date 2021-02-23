class Solution:                 #81. 搜索旋转排序数组 II(中间截开互换位置)
    def search(self, nums, target):         #第一步用二分法，而后顺序查找（可可以先找到旋转位置，这样接下来也使用二分法查找）
        leng = len(nums)
        if target == nums[0]:
           return True
        elif target > nums[0]:
            for i in range(leng):
                if nums[i] == target:
                    return True
                elif target < nums[i]:
                    return False
        elif target < nums[0]:
            for i in range(leng-1,-1,-1):
                if nums[i] == target:
                    return True
                elif target > nums[i]:
                    return False
        return False
nums = [1]
print(Solution().search(nums,0))