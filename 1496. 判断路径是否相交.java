class Solution {
    public boolean isPathCrossing(String path) {
        if(path.length()<4) return false;
        int[][] re = new int[10000][10000];         //一个二位平面（内存溢出！！！）
        re[0][0] = 1;
        int x = 0,y = 0;
        for(int i=0; i<path.length(); i++){
            if(path.charAt(i)=='W'){
                y += 1;
                if(re[x][y] == 1) return true;
            }else if(path.charAt(i)=='S'){
                y -= 1;
                if(re[x][y] == 1) return true;
            }else if(path.charAt(i)=='E'){
                x += 1;
                if(re[x][y] == 1) return true;
            }else{
                x -= 1;
                if(re[x][y] == 1) return true;
            }
            re[x][y] = 1;
        }
        return false;
    }
}

class Solution1 {
    //Hash表查找
    public boolean isPathCrossing(String path) {
        Set<Integer> vis = new HashSet<Integer>();

        int x = 0, y = 0;
        vis.add(getHash(x, y));

        int length = path.length();
        for (int i = 0; i < length; i++) {
            char dir = path.charAt(i);
            switch (dir) {
                case 'N': --x; break;
                case 'S': ++x; break;
                case 'W': --y; break;
                case 'E': ++y; break;
            }
            int hashValue = getHash(x, y);
            if (!vis.add(hashValue)) {
                return true;
            }
        }

        return false;
    }

    public int getHash(int x, int y) {
        return x * 10000 + y;       //（数组的长度时10000）最多就走10000步（为了使x和y的表示唯一）
    }
}
