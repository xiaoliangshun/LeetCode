class Solution {
    public boolean detectCapitalUse(String word) {
        for (int i=0; i<word.length()-1; i++){
            if(i==0 && word.charAt(i)<=90 && word.charAt(i+1)>=97){         //第一个的特殊判断
                continue;
            }else if(word.charAt(i)>=97 && word.charAt(i+1)<=90){       //前边小写后边大写
                return false;
            }else if(word.charAt(i)<=90 && word.charAt(i+1)>=97){     //前边大写后边小写
                return false;
            }
        }
        return true;
    }
}