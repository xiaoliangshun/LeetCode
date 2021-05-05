import java.util.Arrays;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    //排序+二分查找
    public String[] findRelativeRanks(int[] nums) {
        int n = nums.length;
        int[] array = new int[n];
        // 拷贝数组
        System.arraycopy(nums, 0, array, 0, n);
        // 对数组进行排序（正序）
        Arrays.sort(array);
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            // 查找当前成绩排第几名
            int index = n - Arrays.binarySearch(array, nums[i]);      //二分
            switch (index) {
                case 1:
                    result[i] = "Gold Medal";
                    break;
                case 2:
                    result[i] = "Silver Medal";
                    break;
                case 3:
                    result[i] = "Bronze Medal";
                    break;
                default:
                    result[i] = String.valueOf(index);
            }
        }
        return result;
    }
}

class Solution1 {
    //TreeMap
    //key 存储成绩，value 存储成绩在数组中的下标。TreeMap 是按照升序进行排序的，所以在遍历集合时，通过计算可以得出当前成绩的排名。
    public String[] findRelativeRanks(int[] nums) {
        int n = nums.length;
        String[] result = new String[n];
        // key 为成绩，value 为成绩在数组中的下标，TreeMap 是按照升序进行排序的
        Map<Integer, Integer> map = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            map.put(nums[i], i);
        }
        int count = 0;
        for (Map.Entry<Integer, Integer> set : map.entrySet()) {
            // 计算成绩的排名
            int ranking = n - count++;
            switch (ranking) {
                case 1:
                    result[set.getValue()] = "Gold Medal";
                    break;
                case 2:
                    result[set.getValue()] = "Silver Medal";
                    break;
                case 3:
                    result[set.getValue()] = "Bronze Medal";
                    break;
                default:
                    result[set.getValue()] = String.valueOf(ranking);
            }
        }
        return result;
    }
}
class Solution3 {
    //计数排序
    //用数组存储
    public String[] findRelativeRanks(int[] nums) {
        int n = nums.length;
        String[] result = new String[n];
        int max = 0;
        // 找出找出最高的成绩（这样就能减少较长的数组）
        for (int num : nums) {
            if (max < num) {
                max = num;
            }
        }
        // 下标为成绩，值为成绩在 nums 数组的下标
        int[] array = new int[max + 1];
        for (int i = 0; i < n; i++) {
            array[nums[i]] = i + 1;
        }
        // 记录当前成绩的排名
        int count = 1;
        for (int i = array.length - 1; i >= 0; i--) {
            if (array[i] != 0) {
                // 根据排名进行赋值
                switch (count) {
                    case 1:
                        result[array[i] - 1] = "Gold Medal";
                        break;
                    case 2:
                        result[array[i] - 1] = "Silver Medal";
                        break;
                    case 3:
                        result[array[i] - 1] = "Bronze Medal";
                        break;
                    default:
                        result[array[i] - 1] = String.valueOf(count);
                }
                count++;
            }
        }
        return result;
    }
}
