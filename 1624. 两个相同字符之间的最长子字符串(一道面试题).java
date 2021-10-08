 class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int length = s.length()-1;      //两个字符的最大差距
        if(length==1) return 0;

        while(length>1){
            for(int i=0; i+length<s.length(); i++){
                if(s.charAt(i)==s.charAt(i+length)) return length-1;
            }
            length--;
        }
        return -1;
    }
}

 class Solution1 {
    public int maxLengthBetweenEqualCharacters(String s) {
        int max=-1;
        Map<Character,Integer> map=new HashMap<>();     //分别存放该元素和下标的位置
        for(int i=0;i<s.length();i++){
            if(map.containsKey(s.charAt(i))){       //在的话保留前边的元素，并记录差距
                max=Math.max(max,i-map.get(s.charAt(i))-1);
            }
            else{       //放入hash
                map.put(s.charAt(i),i);
            }
        }
        return max;
    }
}

