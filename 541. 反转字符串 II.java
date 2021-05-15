class Solution {
    public String reverseStr(String s, int k) {
        char[] a = s.toCharArray();             //转化成数组形式处理
        for (int start = 0; start < a.length; start += 2 * k) {
            int i = start, j = Math.min(start + k - 1, a.length - 1);       //保证j的下标不越界
            while (i < j) {
                char tmp = a[i];
                a[i++] = a[j];
                a[j--] = tmp;
            }
        }
        return new String(a);
    }
}
