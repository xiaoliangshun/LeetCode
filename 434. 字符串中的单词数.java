class Solution {
    public int countSegments(String s) {
        int segmentCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if ((i == 0 || s.charAt(i-1) == ' ') && s.charAt(i) != ' ') {
                segmentCount++;                             //前边是空格，后边不是空格就算一个单词
            }
        }
        return segmentCount;
    }
}
class Solution1 {
    //使用split分割
    public int countSegments(String s) {
        String trimmed = s.trim();          //去掉两端的多余空格
        if (trimmed.equals("")) {
            return 0;
        }
        return trimmed.split("\\s+").length;
        //    \s匹配任何空白字符，包括空格、制表符、换页符等
        //    “\s+”则表示匹配任意多个上面的字
    }
}
//    split(String regex, int limit)
//        regex -- 正则表达式分隔符。
//        limit -- 分割的份数。