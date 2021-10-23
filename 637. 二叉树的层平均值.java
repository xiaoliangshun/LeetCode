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
    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<Double> l = new ArrayList();
        if(root==null) return l;
        queue.offer(root);
        while(!(queue.isEmpty())){
            int size = queue.size();
            double sum = 0;
            for(int i=0; i<size; i++){
                TreeNode t = queue.remove();
                sum += t.val;
                if(t.left != null) queue.offer(t.left);
                if(t.right != null) queue.offer(t.right);
            }
            l.add(sum /size);
        }
        return l;
    }
}