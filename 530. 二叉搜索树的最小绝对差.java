class Solution {
    int sub = Integer.MAX_VALUE;
    int pre = -1;           //保持前驱节点

    public int getMinimumDifference(TreeNode root) {
        Tree(root);
        return sub;
    }

    public void Tree(TreeNode root){
        if(root == null) return;
        Tree(root.left);
        if(pre == -1){
            pre = root.val;
        }else{
            sub = Math.min(root.val-pre,sub);        //比较谁更小
            pre = root.val;
        }
        Tree(root.right);
    }
}