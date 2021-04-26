class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        int times = (maxChoosableInteger+1);
        if (desiredTotal % times == 0){
            return false;           //后手赢
        }else {
            return true;            //先手赢
        }
    }
}
        //分析：我们可以将数组[1-n]分成n/2个和times相等的整数对
        //如果desiredTotal是times的整数倍，那么只要后手保证每次与先手的和正好为times，后手就一定能赢
        //另一种情况就不是times的整数倍，先手先选择余数，那么就成为了后手。
        //还有就是考虑到如果n为奇数，n是times的整数倍,
        //  后手不要选择中间的那个数，因为只有一个，不能构成整数对，如果对方选择了，那么就选择大于中间的一个数，后哦变就一样了
        //n为奇数，n不是times的整数倍
        //此时先手一样是选择余数，结果就和上边一样了
        //这两种情况与前两种情况一样，无需特殊处理。

        //结果有问题