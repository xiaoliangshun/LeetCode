class Solution {
    public List<String> commonChars(String[] words) {
        int[] minfreq = new int[26];
        Arrays.fill(minfreq,Integer.MAX_VALUE);
        for(String word: words){
            int[] freq = new int[26];
            for(int i=0; i<word.length(); i++){			//计数
                freq[word.charAt(i)-'a']++;
            }
            for(int i= 0; i<26; i++){                //更新每个字母出现的最小次数
                minfreq[i] = Math.min(minfreq[i],freq[i]);
            }
        }

        List<String> s = new ArrayList<String>();		//自增长的数组
        for(int i=0; i<26; i++){
            for(int j=0; j<minfreq[i]; j++){
                s.add(String.valueOf((char)(i+'a')));
            }
        }
        return s;
    }    
}