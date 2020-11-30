class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
        def isSymmetric(self, nums) -> bool:             #当输入为树对用的数组时，可以使用此法：：对每树的每一层进行回文对比
            def isReverse(nums):
                print(nums)
                l =0; r = len(nums)-1
                while l<r:
                    if nums[l] != nums[r]:
                        print(False)
                        return False
                    else:
                        l += 1;r -= 1
                print(True)
                return True
            i = 1
            while 2**i < len(nums):
                if isReverse(nums[2*i-1:2*i+2**i-1]):            #判断是否为回文
                    i += 1
                else:
                    return False
            return True

    def isSymmetric2(self, root: TreeNode) -> bool:              #错误解法：本题要求的是关于最中间的地方对称，而不是每颗子树的左右孩子对称
        def isSym(root):
            if root.left == None and root.right == None:              #叶子节点
                return True

            if root.left != None and root.right ==None  or  root.left == None and root.right != None:          #不对称的情况
                return False
            elif root.right == root.right:               #左右都存在且相等
                return isSym(root.left) and isSym(root.right)
            else:                                         #左右都存在但是不相等
                return False
        # return isSym(root)

        def isSymmetric3(self, root: TreeNode) -> bool:              #可以复制一个同样的树，对比相应的位置
            def isSym(r1,r2):
                if r1 == None and r2 == None:              #叶子节点
                    return True
                elif r1 == None or r2 == None:           #不对称的情况
                    return False
                else:                  #左右都存在且相等
                    r1.val == r2.val and isSym(r1.left,r2.right) and isSym(r1.right,r2.left)             #对称
            return isSym(root,root)                     #要return才行
                    #在我们调用类方法时，类中的self会替换成类的实例。所以在递归时，要想在类下的第一层方法递归，要加上【self.方法明】，或在第一层方法下再来一层

-----------------#也可以使用一个队列实现，先复制两个镜像，一个从左到右输出一个从右到左输出，对比有什么不同，，，跟方法以的判断每层回文相似

nums =[1,2,2,3,4,4,3]
print(Solution().isSymmetric(nums))
