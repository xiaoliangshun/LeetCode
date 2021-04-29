import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    //1.hash
    //2.可以用String的contains方法
    //3.使用String的indexOf方法，找到单词中的每个元素是否在同一个index中（第一行，第二行，第三行）
    public String[] findWords(String[] words) {
        String s1 = "qwertyuiop";
        String s2 = "asdfghjkl";
        String s3 = "zxcvbnm";
        Map<Character,Integer> map = new HashMap<>();           //map,将每一行的字母都输进去
        for (int i=0; i<s1.length(); i++){
            map.put(s1.charAt(i),1);
        }
        for (int i=0; i<s2.length(); i++){
            map.put(s2.charAt(i),2);
        }
        for (int i=0; i<s3.length(); i++){
            map.put(s3.charAt(i),3);
        }
//        String[] ss = new String[words.length];           //静态
        List<String> li = new ArrayList<String>();          //动态
        for(String word : words){
            StringBuilder sb = new StringBuilder(word.toLowerCase());       //将其变成小写
            boolean b = true;
            for (int i=1; i<word.length(); i++){
                if(map.get(sb.charAt(i)) != map.get(sb.charAt(i-1))){
                    b = false;
                    break;
                }
            }
            if (b) li.add(word);
        }
        return (String[])li.toArray(new String[li.size()]);
    }
}
class Solution2 {
    public String[] findWords(String[] words) {

        String string1 = "qwertyuiop";
        String string2 = "asdfghjkl";
        String string3 = "zxcvbnm";

        ArrayList<String> list = new ArrayList<>();
        for (String word : words) {
            String word1 = word.toLowerCase();
            char c = word1.charAt(0);
            if (string1.contains(String.valueOf(c))){
                if (check(word1,string1)){
                    list.add(word);
                }
            }else if (string2.contains(String.valueOf(c))){
                if (check(word1,string2)){
                    list.add(word);
                }
            }else if (string3.contains(String.valueOf(c))){
                if (check(word1,string3)){
                    list.add(word);
                }
            }
        }
        String[] result = new String[list.size()];
        return list.toArray(result);
    }

    public boolean check(String word,String string){
        for (int i = 1; i < word.length(); i++) {
            if (!string.contains(String.valueOf(word.charAt(i)))){      //contains方法
                return false;
            }
        }
        return true;
    }

}

