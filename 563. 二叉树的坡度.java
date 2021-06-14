/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum = 0;
    public int find(TreeNode root){     //包含根节点的树和
        if(root==null) return 0;
        int sum1 = find(root.left); 
        int sum2 = find(root.right);
        sum += Math.abs(sum1-sum2);     //记录
        return sum1+sum2+root.val;          //子树和
    }

    public int findTilt(TreeNode root) {
        find(root);
        return sum;
    }
}




