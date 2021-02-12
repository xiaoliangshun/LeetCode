class Solution:
    def singleNumber(self, nums):       #HashMap
        dict1 = dict()
        for x in nums:
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1
        for key,value in dict1.items():
            if value == 1:
                return key
##法2：HashSet
#3×(a+b+c)−(a+a+a+b+b+b+c)=2c
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2

nums = [0,1,0,1,0,1,99]
print(Solution().singleNumber(nums))