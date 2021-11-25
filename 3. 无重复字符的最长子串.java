package com.xls;

import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        //1.现将nums1的元素使用hashMap计数
        //2.使用nums2的每一个元素进行查找
        HashMap<Integer, Integer> hm = new HashMap();
        for (int i = 0; i < nums1.length; i++) {
            int count = hm.getOrDefault(nums1[i], 0) + 1;       //hm中nums1[i]为null时，默认为0，否则就是原来的值
            hm.put(nums1[i],count);
        }

        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 0; i <nums2.length; i++) {
            if(hm.containsKey(nums2[i])){
                res.add(nums2[i]);
                if(hm.get(nums2[i])==1){
                    hm.remove(nums2[i]);
                }else {
                    hm.put(nums2[i], hm.get(nums2[i]) - 1);
                }
            }
        }
        int[] ints = new int[res.size()];
//        System.arraycopy(res,0,ints,0,res.size());      //数组拷贝
        for (int i = 0; i < res.size(); i++) {
            ints[i] = res.get(i);
        }
        return ints;
    }
}

//还可以使用排序+双指针归并
