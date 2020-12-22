# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list1 = list()
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            list1.append(root.val)
            inorder(root.right)
        inorder(root)
        return list1

#     栈
#     思路与算法
#
#     方法一的递归函数我们也可以用迭代的方式实现，两种方式是等价的，区别在于递归的时候隐式地维护了一个栈，
#     而我们在迭代的时候需要显式地将这个栈模拟出来，其他都相同。
#
#     class Solution {
#     public List < Integer > inorderTraversal(TreeNode root) {
#     List < Integer > res = new ArrayList < Integer > ();
#     Deque < TreeNode > stk = new LinkedList < TreeNode > ();
#
#     while (root != null | | !stk.isEmpty()) {
#     while (root != null) {
#       stk.push(root);
#       root = root.left;       #左侧全部入栈
#     }
#     root = stk.pop();         #出栈+带入右子树
#     res.add(root.val);
#     root = root.right;
# }
# return res;
# }
# }
