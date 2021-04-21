class Solution {
    public int longestPalindrome(String s) {
        int[] a = new int[58];        //a：97  A：65       表示从65--97+26的字母
        boolean b = false;          //表示是否已经计算奇数了
        int sum = 0;
        for (int i=0; i<s.length(); i++){
            a[s.charAt(i)-'A']++;
        }

        for (int i=0; i<a.length; i++){
            if (!b && a[i] % 2 == 1){
                sum += 1;
                b = true;
            }
            sum += (a[i] / 2)*2;            //不管奇数还是偶数
        }
        return sum;
    }
}