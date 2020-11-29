class Solution:
    def maxSubArray(self, nums):            #---------------借鉴-----将问题化小，在前一个问题的基础上求解（延伸）
        for i in range(1,len(nums)):
            nums[i] = nums[i] + max(0,nums[i-1])      #最大的连续数两边加的必然是正数----
        return max(nums)


nums =[10,-4,2,-1,1]
print(Solution().maxSubArray(nums))
