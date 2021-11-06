class Solution {
    public int countSubstrings(String s) {
		//中心扩散算法，
        int n = s.length(), ans = 0;
        for (int i = 0; i < 2 * n - 1; ++i) {
            int l = i / 2, r = i / 2 + i % 2;		//其中这里刚好将所有的情况都分出来了，当i为奇数时：l与r相同；当i为偶数时：l+1与r相同；-->实现了偶数和奇数的同时表示
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                --l;
                ++r;
                ++ans;
            }
        }
        return ans;
    }
}

   //马拉车算法？？