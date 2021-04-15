class Solution {
     // 法1：hash表存储（计数）
    public char findTheDifference(String s, String t) {
        int[] a = new int[26];
        for (int i=0; i<s.length(); i++){
            a[s.charAt(i)-'a'] += 1;
        }
        for (int i=0; i<t.length(); i++){
            if (a[t.charAt(i)-'a']==0){
                return t.charAt(i);
            }else{
                a[t.charAt(i)-'a'] -= 1;
            }
        }
        return 'a';     //没用
    }

    //法2：使用ASCII码求和，做减法
    public char findTheDifference2(String s, String t){
        int sum = 0;
        for (int i=0; i<t.length(); i++){
            sum += t.charAt(i);          //相加的和为ASCII码的和 （字符串相加就是连接操作）
        }
        for (int i=0; i<s.length(); i++){
            sum -= s.charAt(i);
        }
        return (char)sum;
    }


    //法3：位运算：将s和t的每一个单词做异或（出现两次的都会被抵消）
    public char findTheDifference3(String s, String t){
        int a = 0;
        for (int i=0; i<t.length(); i++){
            a ^= t.charAt(i);
        }
        for (int i=0; i<s.length(); i++){
            a ^= s.charAt(i);
        }
        return (char)a;
    }
}