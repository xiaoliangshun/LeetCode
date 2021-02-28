class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()                         #排序
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    def containsDuplicate(self, nums: List[int]) -> bool:     ##哈希表(空间换时间)
        dict1 = dict()
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                return True
        return False
