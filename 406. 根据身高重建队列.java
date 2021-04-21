class Solution {
    public int[][] reconstructQueue(int[][] people) {
        //第一个元素我们可以确定：是ki为0中hi最小的那个
        //选择出第一个之后，我们将剩余的人中hi小于等于前一个hi的ki都减去1(这样做我们就相当于忽视了第一个元素)
        //循环上述操作
        //有点小问题？？？？？？
        int current = 0;            //当前交换的位置
        int index = 0;          //在最前边的元素下标
        while (current != people.length){
            int min_h = 10^6;
            for (int i=current; i<people.length; i++){            //找到ki为0，hi最小的元素
                if (people[i][1] == 0){
                    if (people[i][0] < min_h){
                        min_h = people[i][0];
                        index = i;
                    }
                }
            }
            int[] a = people[index];                                //将这个元素放在前边
            people[index] = people[current];
            people[current] = a;
            current++;
            for(int i=current; i<people.length; i++){               //将剩余的人中hi小于等于前一个hi的ki都减去1
                if (people[i][0] <= people[current-1][0]){
                    people[i][1]--;
                }
            }
        }
        //由于我们在计算过程中对ki进行了-1,最后还要恢复
        for(int i=1; i<people.length; i++){
            int myh = people[i][0];
            if (myh >= people[i-1][0]){
                people[i][1] = people[i-1][0] + 1;
                continue;
            }
            for (int j=0; j<i; j++){
                if (people[j][0] >= myh){
                    people[i][1]++;
                }
            }
        }
        return people;
    }
}

//先排序后插队
//渔（套路）：一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。
//        在本题目中，我首先对数对进行排序，按照数对的元素 1 降序排序，按照数对的元素 2 升序排序。
//        原因是，按照元素 1 进行降序排序，对于每个元素，在其之前的元素的个数，就是大于等于他的元素的数量，
//        而按照第二个元素正向排序，我们希望 k 大的尽量在后面，减少插入操作的次数。（也可以不排序）
//class Solution:
//        def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
//        res = []
//        people = sorted(people, key = lambda x: (-x[0], x[1]))
//        for p in people:
//        if len(res) <= p[1]:          #直接插入(前边都没有那么多高个子)【在此之前比他高的人都已经进来了】
//        res.append(p)                     #较高的元素其实优先级更低，因为比它低的元素放在它前边或者后边都不影响它
//        elif len(res) > p[1]:         #插队
//        res.insert(p[1], p)
//        return res
