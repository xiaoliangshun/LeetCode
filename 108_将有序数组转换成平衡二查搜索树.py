# class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def ToTree(nums):
            leng = len(nums)
            if leng == 0:
                return None
            index = leng // 2           #是偶数的话为对称点的后一个(数组从0开始的))
            root = TreeNode(nums[index])
            root.left = ToTree(nums[:index])
            root.right = ToTree(nums[index+1:])
            return root
        return ToTree(nums)