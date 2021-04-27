class Solution {
    public int[] constructRectangle(int area) {
        int[] re = new int[2];
        int a = (int) Math.floor(Math.sqrt(area));
        while (a<=area){
            if(area % a == 0){
                re[0] = a;
                re[1] = area/a;
                if (re[0]>=re[1]) return re;
            }
            a++;            //长度增加
        }
        return re;
    }

    //一样的思路别人的代码
    public int[] constructRectangle2(int area) {
        int sqrt = (int) Math.sqrt(area);
        if (sqrt * sqrt == area) {
            return new int[]{sqrt, sqrt};
        }
        for (int i = sqrt; i >= 1; i--) {
            if (area % i == 0) {
                return new int[]{area / i, i};
            }
        }
        return null;
    }

    public int[] constructRectangle3(int area) {
        int length = (int)Math.sqrt(area), width = length;
        while (length < area && width > 1) {
            int product = length * width;
            if (product == area) {
                return new int[]{length, width};
            }
            else if (product < area) {      //双向找
                length++;
            } else {
                width--;
            }
        }
        return new int[]{area, 1};
    }
}