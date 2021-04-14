class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] a = new int[26];
        for (int i=0; i<magazine.length(); i++){
            a[magazine.charAt(i)-'a'] ++;
        }
        for (int i=0; i<ransomNote.length(); i++){
            if (a[ransomNote.charAt(i)-'a'] == 0){          //charAt返回在ransomNote中第i个字符
                return false;
            } else{
                a[ransomNote.charAt(i)-'a'] -= 1;
            }
        }
        return true;
    }
}