public class Solution {
    //暴力解法：将2**n种的字符串全放在hashMap中，找到其中只出现一次的最长序列
    public int findLUSlength(String[] strs) {
        HashMap < String, Integer > map = new HashMap < > ();
        for (String s: strs) {
            for (int i = 0; i < (1 << s.length()); i++) {
                String t = "";
                for (int j = 0; j < s.length(); j++) {
                    if (((i >> j) & 1) != 0)
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

class Solution1 {
    //检查所有字符是不是别的字符的子串
    public boolean isSubsequence(String x, String y) {
        int j = 0;
        for (int i = 0; i < y.length() && j < x.length(); i++)
            if (x.charAt(j) == y.charAt(i))
                j++;
        return j == x.length();
    }
    public int findLUSlength(String[] strs) {
        int res = -1;
        for (int i = 0, j; i < strs.length; i++) {
            for (j = 0; j < strs.length; j++) {
                if (j == i)
                    continue;
                if (isSubsequence(strs[i], strs[j]))    //是否是子串
                    break;
            }
            if (j == strs.length)
                res = Math.max(res, strs[i].length());
        }
        return res;
    }
}

public class Solution2 {
    //在上边的方法上，先按照长度的降序进行排序，这样的话如果从前到后匹配，是独特的话，就直接返回
    public boolean isSubsequence(String x, String y) {
        int j = 0;
        for (int i = 0; i < y.length() && j < x.length(); i++)
            if (x.charAt(j) == y.charAt(i))
                j++;
        return j == x.length();
    }
    public int findLUSlength(String[] strs) {
        Arrays.sort(strs, new Comparator < String > () {
            public int compare(String s1, String s2) {
                return s2.length() - s1.length();
            }
        });
        for (int i = 0, j; i < strs.length; i++) {
            boolean flag = true;
            for (j = 0; j < strs.length; j++) {
                if (i == j)
                    continue;
                if (isSubsequence(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                return strs[i].length();
        }
        return -1;
    }
}

