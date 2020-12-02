from functools import reduce
class Solution:
    def singleNumber(self, nums):
        print(max(nums))
        minn = min(nums)
        list1 = [0]*(max(nums)+1-minn)              #最小值放在数组的最左边（空间复杂度很高）
        for num in nums:
            list1[num-minn] += 1
        for i in range(len(list1)):
            if list1[i] == 1:
                return i+minn
    def singleNumber2(self, nums):           #还是使用的数组
        list1 = list()
        for i in range(len(nums)):
            if nums[i] in list1:
                list1.remove(nums[i])                     #del、pop根据索引值删除，remove根据值删除、clear删除全部
            else:
                list1.append(nums[i])
        return list1[0]
    def singleNumber3(self,nums):            #使用集合set操作
        set1 = set()
        for num in nums:
            if num in set1:                 #有一对就删除
                set1.remove(num)
            else:
                set1.add(num)
        return set1
    def singleNumber4(self,nums):                   #使用hash操作
        dict1 = {}
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        for key,value in dict1.items():
            if value == 1:
                return key
    def singleNumber5(self,nums):             #只有一个元素是单个的，那么用集合将所有的数求和再乘2，减去原数组的和就能求到
        set1 = set(nums)
        return sum(set1)*2-sum(nums)

    def singleNumber6(self,nums):   #-----------------------位运算(&、|、^、⊕)--------------------------------------
                ##########-------------时间复杂度O(n),空间复杂度O(1)
                # 可使用异或运算⊕。异或运算有以下三个性质.任何数和0做异或运算，结果仍然是原来的数，即a⊕0 = a。
                # 任何数和其自身做异或运算，结果是0，即 a⊕a = 0。
                # 异或运算满足交换律和结合律，即: a⊕b⊕a = b⊕a⊕a = b⊕(a⊕a) = b⊕0 = b。
        return reduce(lambda x, y: x ^ y, nums)             #要导包：from functools import reduce

prices = [4,1,2,1,2]
print(Solution().singleNumber6(prices))