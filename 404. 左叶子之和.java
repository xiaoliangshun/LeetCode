//public class TreeNode {
//     int val;
//     TreeNode left;
//     TreeNode right;
//     TreeNode() {}
//     TreeNode(int val) { this.val = val; }
//     TreeNode(int val, TreeNode left, TreeNode right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
//}

class Solution {
    //我的深度优先
    public int sumOf(TreeNode root,int sum){
        if (root == null){
            return 0;
        }
        if(root.left == null){
            sum += root.val;
            sum += sumOf(root.right,sum);
        }else{
            sum += sumOf(root.left,sum);
            sum += sumOf(root.right,sum);
        }
        return sum;
    }

    public int sumOfLeftLeaves(TreeNode root) {
        int sum = sumOf(root,0);
        return sum;
    }
}


class Solution1 {
    //答案上的深度优先
    public int sumOfLeftLeaves(TreeNode root) {
        return root != null ? dfs(root) : 0;
    }

    public int dfs(TreeNode node) {
        int ans = 0;
        if (node.left != null) {               //判断左孩子是否是左叶子节点
            ans += isLeafNode(node.left) ? node.left.val : dfs(node.left);
        }
        if (node.right != null && !isLeafNode(node.right)) {        //判断右孩子是否是叶子节点
            ans += dfs(node.right);
        }
        return ans;
    }

    public boolean isLeafNode(TreeNode node) {
        return node.left == null && node.right == null;
    }
}

class Solution2 {
    //广度优先
    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        int ans = 0;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();               //出队
            if (node.left != null) {            //左孩子入队
                if (isLeafNode(node.left)) {
                    ans += node.left.val;
                } else {
                    queue.offer(node.left);
                }
            }
            if (node.right != null) {           //右孩子入队
                if (!isLeafNode(node.right)) {
                    queue.offer(node.right);
                }
            }
        }
        return ans;
    }

    public boolean isLeafNode(TreeNode node) {
        return node.left == null && node.right == null;
    }
}



