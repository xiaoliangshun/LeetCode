class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## 数学方法
        n = len(nums)
        sum = n*(n+1)/2     # 表示从0-n的所有数之和
        for i in range(n):
            sum -= nums[i]
        return int(sum)

    ## 法2 也可以使用排序的方法 找哪里是不连续的

    ## 法3 哈希表（查询的时间复杂度为O（1））   现将nums的所有元素放入hash中，查找0-n是否都在其中
                                        # 或者现将0-n全部放进hash中，遍历nums数组，将hash中存在的全部删除，那么剩余的最后一个就是

    # 法4 使用异或操作，因为任何一个数与相同的数异或两次还是它自己，
    # 这样的话就将nums中的所有元素异或后再与（0-n）异或 ,相当于将净nums的元素映射到（0-n）上看那个没有