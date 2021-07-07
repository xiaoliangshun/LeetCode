class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        //没有优化，笨拙
        HashMap<String,Integer> hm1 = new HashMap<String,Integer>();
        HashMap<String,Integer> hm2 = new HashMap<String,Integer>();
        String[] ss1 = s1.split(" ");
        String[] ss2 = s2.split(" ");
        for(String word : ss1){
            if(!hm1.containsKey(word)){
                hm1.put(word,1);
            }else{
                hm1.put(word,2);
            }        
        }
        for(String word : ss2){
            if(!hm2.containsKey(word)){
                hm2.put(word,1);
            }else{
                hm2.put(word,2);
            } 
            // System.out.println(word+hm2.get(word));
        }
        ArrayList<String> al = new ArrayList<String>(); 
        for(String word : ss1){
            if(hm1.get(word)==1 && !hm2.containsKey(word)){
                al.add(word);
                // System.out.println(word);
            }
        }
        for(String word : ss2){
            if(hm2.get(word)==1 && !hm1.containsKey(word)){
                al.add(word);
            }
        }
        String[] re = new String[al.size()];
        for(int i=0; i<al.size(); i++){
            // System.out.println(al.get(i));
            re[i] = al.get(i);
        }
        return re;
    }
}

class Solution {
    //官方解法
    public String[] uncommonFromSentences(String A, String B) {
        Map<String, Integer> count = new HashMap();
        for (String word: A.split(" "))
            count.put(word, count.getOrDefault(word, 0) + 1);
        for (String word: B.split(" "))
            count.put(word, count.getOrDefault(word, 0) + 1);

        List<String> ans = new LinkedList();
        for (String word: count.keySet())       //只出现一次，并且在另一个字符串中并没有出现，完全可以用一个hash来代替
            if (count.get(word) == 1)
                ans.add(word);

        return ans.toArray(new String[ans.size()]);
    }
}
