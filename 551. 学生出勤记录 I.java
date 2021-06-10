class Solution {
    public boolean checkRecord(String s) {
        int count_A = 0;	//记录A的数量
        int count_L = 0;	//记录连续L的数量（在遇到非A时归0）
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == 'A'){
                count_A++;
                count_L = 0;		
            }else if(s.charAt(i) == 'L'){
                count_L++;
            }else{
                count_L = 0;
            }
            if(count_A>1 || count_L>2) return false;
        }
        return true;
    }
}