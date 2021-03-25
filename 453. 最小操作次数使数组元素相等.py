
            ##排序
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()         ##在原数组上操作（其实只用了最小值，不用排序————》时间复杂度就变成O（n）了）
        count = 0
        for i in range(len(nums)):
            count += nums[i] - nums[0]
        return count
        # n-1个元素在加，一个元素不变
        # 其中的n-1个元素的相对位置肯定是不会变的，而且我们每次一定是让最大的值保持不变，其余的数加1
        # 最小的数的肯定是一直在加的，只有让最大值直接变成最小值之后，这两个值就一样了，只用跟着一起加就可以了
        # 让其与的n-2个值也依次变成最小值
        # 这样移动的此时就是所有值与最小值的差了

##将除了一个元素之外的全部元素+1，等价于将该元素-1，因为我们只对元素的相对大小感兴趣。因此，该问题简化为需要进行的减法次数。
    #


    ##动态规划
    #其实是先把最小值升到次小值一样的位置后（这样会倒置次小值与次次小值之间的差距拉开，在计算下一次时应该加上上一次的拉近到原来位置的操作），继续操作
# public class Solution {
#     public int minMoves(int[] nums) {
#         Arrays.sort(nums);
#         int moves = 0;
#         for (int i = 1; i < nums.length; i++) {
#             int diff = (moves + nums[i]) - nums[i - 1];
#             nums[i] += moves;
#             moves += diff;
#         }
#         return moves;
#     }
# }