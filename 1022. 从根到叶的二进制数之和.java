class Solution {
    int sum = 0;
    public void rootToLeaf(TreeNode root, int a){
        if (root == null) return;
        a = (a << 1) + root.val;
        if (root.left == null && root.right == null) sum += a;

        rootToLeaf(root.left,a);
        rootToLeaf(root.right,a);
    }
    public int sumRootToLeaf(TreeNode root) {
        rootToLeaf(root,0);
        return sum;
    }
}