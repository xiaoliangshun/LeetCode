/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        if(root==null) return 0;
        int MaxD = 0; 
        for(Node r: root.children){		//递归遍历
            MaxD = Math.max(maxDepth(r),MaxD);
        }
        return MaxD+1;		//返回最深的+1
    }
}