class Solution {
    public String convertToBase7(int num) {
        StringBuilder sb = new StringBuilder();
        int minus = 1;
        num = Math.abs(num);
        while(num>0){
            sb.insert(0,num%7);
            num /= 7;
        }
        if (num<0) sb.insert(0,'-');
        return sb.toString();
    }
}
