# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):                     ##前序+中序构造一颗二叉树（修改成功）
        def bulid(preorder, inorder):
            if len(inorder) == 1:
                return TreeNode(preorder[0])
            elif len(inorder) > 1:
                root_val = preorder[0]
                fen = inorder.index(root_val)       ##查找值为root元素的下标（可以通过字典建立hash表，加快定位）

                root = TreeNode(root_val)  # 创建一个节点
                root.left = bulid(preorder[1:fen + 1], inorder[:fen])
                root.right = bulid(preorder[fen + 1:], inorder[fen + 1:])
                return root
        return bulid(preorder, inorder)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:              #后续+中序构造一颗二叉树
        def build(inorder,postorder):
            if len(inorder) == 0:
                return None
            else:
                # print(postorder[-1])
                mid = inorder.index(postorder[-1])      #在中序遍历中的分界线
                root = TreeNode(postorder[-1])
                root.left = build(inorder[:mid],postorder[:mid])                 #划分
                root.right = build(inorder[mid+1:],postorder[mid:len(postorder)-1])
                return root
        return build(inorder,postorder)



print(Solution().zigzagLevelOrder(root))