class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0;              //i,j 指向待匹配元素的位置
        int j = 0;
        while (i<s.length() && j<t.length()){
             if (s.charAt(i) == t.charAt(j)){
                 i++;
                 j++;
             }else{
                 j++;
             }
        }
        if (i == s.length()){
            return true;
        }
        return false;
    }

    //或动态规划：对于单个s的查找没有什么什么优势，但是对于多个s的查找则只用一次刚开始的预处理
    //f[i][j]表示串t的第i个元素后j（26个字母a-z）出现的位置
    //当t[i] == j时;  f[i][j]=i
    //当t[i] != j时;  f[i][j]=f[i+1][j]     （这样的话我就够倒着动态规划了）
        public boolean isSubsequence2(String s, String t) {
            int n = s.length(), m = t.length();

            int[][] f = new int[m + 1][26];
            for (int i = 0; i < 26; i++) {
                f[m][i] = m;
            }

            for (int i = m - 1; i >= 0; i--) {
                for (int j = 0; j < 26; j++) {
                    if (t.charAt(i) == j + 'a')
                        f[i][j] = i;
                    else
                        f[i][j] = f[i + 1][j];
                }
            }
            int add = 0;
            for (int i = 0; i < n; i++) {
                if (f[add][s.charAt(i) - 'a'] == m) {
                    return false;
                }
                add = f[add][s.charAt(i) - 'a'] + 1;
            }
            return true;
        }

}
