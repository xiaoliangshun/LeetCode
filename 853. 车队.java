        //方案1：按照车队离终点的距离排序，计算相邻两个赶上的时间，取之中最小的那个，将时间往后推到这个位置,合并这几辆车（继续循环）
        //方案2：计算每个车到达终点的时间，将最短的去掉作为一个车队，时间往后推
        
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int N = position.length;
        Car[] cars = new Car[N];
        for (int i = 0; i < N; ++i)
            cars[i] = new Car(position[i], (double) (target - position[i]) / speed[i]);
        Arrays.sort(cars, (a, b) -> Integer.compare(a.position, b.position));       //按位置大小排序

        int ans = 0, t = N;
        while (--t > 0) {
            if (cars[t].time < cars[t-1].time) ans++; //if cars[t] arrives sooner, it can't be caught（单独的一个车队）
            else cars[t-1] = cars[t]; //else, cars[t-1] arrives at same time as cars[t]（形成车队，按照行驶时间长的来计算）
        }

        return ans + (t == 0 ? 1 : 0); //lone car is fleet (if it exists)
    }
}

class Car {
    int position;
    double time;
    Car(int p, double t) {
        position = p;
        time = t;
    }
}

// 作者：LeetCode
// 链接：https://leetcode-cn.com/problems/car-fleet/solution/che-dui-by-leetcode/
// 来源：力扣（LeetCode）