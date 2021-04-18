import java.util.ArrayList;
import java.util.List;

class Solution {
    int[] hours = new int[]{1, 2, 4, 8, 0, 0, 0, 0, 0, 0};          //数组的巧妙处理方法
    int[] minutes = new int[]{0, 0, 0, 0, 1, 2, 4, 8, 16, 32};
    List<String> res = new ArrayList<>();

    public List<String> readBinaryWatch(int num) {
        backtrack(num, 0, 0, 0);
        return res;
    }

    public void backtrack(int num, int index, int hour, int minute){
        if(hour > 11 || minute > 59)           //特殊判断
            return;
        if(num == 0){                       //最后一个的情况
            StringBuilder sb = new StringBuilder();
            sb.append(hour).append(':');
            if (minute < 10) {
                sb.append('0');
            }
            sb.append(minute);
            res.add(sb.toString());
            return;
        }
        for(int i = index; i < 10; i++){                //num表示要亮LED灯的数量，index为开始的位置
            backtrack(num - 1, i + 1, hour + hours[i], minute + minutes[i]);
            // 表示从index开始挑num个指示灯，每次递归从i+1开始避免了重复（后边的又选了前边的）
        }
    }
}
