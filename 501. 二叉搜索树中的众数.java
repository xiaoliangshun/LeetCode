class Solution {
    //我的，没有考虑多个的情况
    public int[] max_frequent(TreeNode root){
        if(root == null){
            return new int[]{0,0};          //第一位表示num，第二位表示出现的次数
        }
        if(root.left==null && root.right==null){
            return new int[]{root.val,1};
        }
        int[] a1 = max_frequent(root.left);
        int[] a2 = max_frequent(root.right);
        if (root.val == a1[0]){
            a1[1]++;
        }else if(root.val == a2[0]){
            a2[1]++;
        }
        return a1[1]>a2[1]?a1:a2;
    }
    public int[] findMode(TreeNode root) {
        int[] aa = max_frequent(root);
        return new int[]{aa[0]};
    }
}

class Solution1 {
    //中序遍历为有序数组，从数组中找
    List<Integer> answer = new ArrayList<Integer>();
    int base, count, maxCount;

    public int[] findMode(TreeNode root) {
        dfs(root);
        int[] mode = new int[answer.size()];
        for (int i = 0; i < answer.size(); ++i) {
            mode[i] = answer.get(i);
        }
        return mode;
    }

    public void dfs(TreeNode o) {
        if (o == null) {
            return;
        }
        dfs(o.left);
        update(o.val);
        dfs(o.right);
    }

    public void update(int x) {
        if (x == base) {
            ++count;
        } else {
            count = 1;
            base = x;
        }
        if (count == maxCount) {
            answer.add(base);
        }
        if (count > maxCount) {
            maxCount = count;
            answer.clear();
            answer.add(base);
        }
    }
}
