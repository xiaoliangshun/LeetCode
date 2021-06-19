public class Solution {
    public int findLHS(int[] nums) {
        HashMap < Integer, Integer > map = new HashMap < > ();      //创建Hash表
        int res = 0;
        for (int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);     //将所有元素放入Hash
        }
        for (int key: map.keySet()) {       //看相邻两个元素的个数和是不是最大
            if (map.containsKey(key + 1))       
                res = Math.max(res, map.get(key) + map.get(key + 1));
        }
        return res;
    }
}
