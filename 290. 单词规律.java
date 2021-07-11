class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if(pattern.length() != words.length) return false;
        for(int i=0; i<pattern.length(); i++){
            for(int j=i+1; j<pattern.length(); j++){
                if(pattern.charAt(i) == pattern.charAt(j)){
                    if(!words[i].equals(words[j])) return false;
                }else{
                    if(words[i].equals(words[j])) return false;
                }
            }
        }
        return true;
    }
}

class Solution {
    public boolean wordPattern(String pattern, String str) {
        // 我们需要判断字符与字符串之间是否恰好一一对应。即任意一个字符都对应着唯一的字符串，任意一个字符串也只被唯一的一个字符对应。在集合论中，这种关系被称为「双射」
		// 一一对应时，pattern中的字符相同则str对应通；不同则也不同       这样就强行让pattern中的规律映射到了str中了
        Map<String, Character> str2ch = new HashMap<String, Character>();
        Map<Character, String> ch2str = new HashMap<Character, String>();
        int m = str.length();
        int i = 0;
        for (int p = 0; p < pattern.length(); ++p) {
            char ch = pattern.charAt(p);
            if (i >= m) {
                return false;
            }
            int j = i;
            while (j < m && str.charAt(j) != ' ') {		//界定单词
                j++;
            }
            String tmp = str.substring(i, j);
            if (str2ch.containsKey(tmp) && str2ch.get(tmp) != ch) {
                return false;
            }
            if (ch2str.containsKey(ch) && !tmp.equals(ch2str.get(ch))) {
                return false;
            }
            str2ch.put(tmp, ch);
            ch2str.put(ch, tmp);
            i = j + 1;
        }
        return i >= m;
    }
}
