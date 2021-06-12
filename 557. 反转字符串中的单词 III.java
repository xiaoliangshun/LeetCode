class Solution {
    public String reverseWord(String s){		//将单词逆转
        String s1 = "";
        for(int i=s.length()-1; i>=0; i--){
            s1 += s.charAt(i);
        }
        return s1;
    }
    public String reverseWords(String s) {
        String[] ss = s.split(" ");				//按照空格分离
        String re = "";
        for(int i=0; i<ss.length; i++){
            re += reverseWord(ss[i]);
            if(i==ss.length-1) break;
            re += " ";
        }
        return re;
    }
}


class Solution1 {
	//使用StringBuffer(Java不能使用原地解法，因为String不可变)
    public String reverseWords(String s) {
        StringBuffer ret = new StringBuffer();
        int length = s.length();
        int i = 0;
        while (i < length) {
            int start = i;
            while (i < length && s.charAt(i) != ' ') {		//找单词
                i++;
            }
            for (int p = start; p < i; p++) {
                ret.append(s.charAt(start + i - 1 - p));		//逆转
            }
            while (i < length && s.charAt(i) == ' ') {
                i++;
                ret.append(' ');
            }
        }
        return ret.toString();
    }
}
