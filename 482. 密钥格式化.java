class Solution {
    public String licenseKeyFormatting(String s, int k) {
        int count = 0;
        StringBuilder sb = new StringBuilder();
        for (int i=s.length()-1; i>=0; i--){
            if(s.charAt(i) == '-'){             //忽略'-'
                continue;
            }else {
                if(count < k) {           //不够k个
                    count++;
                }else {                   //已经够k个了，先记录，
                    sb.insert(0,'-');
                    count = 1;
                }
                sb.insert(0,s.charAt(i));           //巴当前元素加进去
            }
        }
        return sb.toString().toUpperCase();            //装换为大写
    }
}