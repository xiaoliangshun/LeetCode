class Solution {
    public int compress(char[] chars) {
        int n = chars.length;
        int write = 0, left = 0;    //读的位置，left为该子串的第1个位置
        for (int read = 0; read < n; read++) {      //写的位置（字符串的最右侧）
            if (read == n - 1 || chars[read] != chars[read + 1]) {      //到结尾其实也应该加上(很好的处理了特殊情况)
                chars[write++] = chars[read];
                int num = read - left + 1;      //之所以要减1，是因为read和后边对比的
                if (num > 1) {
                    String s = num+"";
                    for(int i=0; i<s.length(); i++){
                        chars[write++] = s.charAt(i);
                    }
                }
                left = read + 1;
            }
        }
        return write;
    }
}