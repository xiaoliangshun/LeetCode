public class Solution {
    public int findLUSlength(String a, String b) {
        HashMap < String, Integer > map = new HashMap < > ();
        for (String s: new String[] {a, b}) {
            for (int i = 0; i < (1 << s.length()); i++) {       //1<<n  :表示2的n次方 （即从0-2^n-1）
                String t = "";
                for (int j = 0; j < s.length(); j++) {
                    if (((i >> j) & 1) != 0)                    //其实是按照i的数值（转化为2进制）对应的每位，看是否要加上对用的字符
                        t += s.charAt(j);
                }
                if (map.containsKey(t))
                    map.put(t, map.get(t) + 1);
                else
                    map.put(t, 1);
            }
        }
        int res = -1;
        for (String s: map.keySet()) {
            if (map.get(s) == 1)
                res = Math.max(res, s.length());
        }
        return res;
    }
}