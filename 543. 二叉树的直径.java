class Solution {
    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 1;
        depth(root);
        return ans - 1;
    }
    public int depth(TreeNode node) {           //不仅计算了节点的深度，也计算了路径上的节点数量（ans-1才是直径）
        if (node == null) {
            return 0; // 访问到空节点了，返回0
        }
        int L = depth(node.left); // 左儿子为根的子树的深度
        int R = depth(node.right); // 右儿子为根的子树的深度
        ans = Math.max(ans, L+R+1); // 计算d_node即L+R+1 并更新ans（带上根节点，所以+1）
        return Math.max(L, R) + 1; // 返回该节点为根的子树的深度(这条路径上节点个数)
    }
}
