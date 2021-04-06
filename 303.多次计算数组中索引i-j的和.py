class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:                    ##计算前缀和，
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]      ##我们要计算的是i到j的之间的元素和，
                    # ，如果提前存储数组的前缀和，那莫时间复杂度就是O（1），因为在创建前缀和数组时已经用了O（n）的时间复杂度
