class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        int matchCount = 0;
        String[] arr = sentence.split("\\s+"); //分割一个或者多个空格
        int i;
        int firstIndex = 0;         //记录第一个下标
        for(i=0; i<arr.length; i++){
            if(arr[i].length()<searchWord.length()) continue;       //无法匹配
            if(arr[i].substring(0,searchWord.length()).equals(searchWord)) {        //看子串
                matchCount++;
                if (firstIndex==0) firstIndex = i+1;        //记录第一个匹配的下标
                if (matchCount > 1) return firstIndex;          //直接返回
            }
        }
        if(matchCount==0) return -1;
        return firstIndex;
    }
}