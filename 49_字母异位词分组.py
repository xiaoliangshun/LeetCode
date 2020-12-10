import collections
class Solution(object):                                #使用字典和排序将相同的，放在一个单元
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)    #------------------------设置字典value中的类型（这里是数组）
        for s in strs:
            ans[tuple(sorted(s))].append(s)                   #排序后如果所含字母一样则必然是同一个，tuple元组（元组才能行）
        return ans.values()

#########法2：上边使用的是每个字母的排序作为标识，这里使用计数对不同的单词进行分类（26位的数组记录每个单词出现的个数）
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1                #按照字母的位置在数组中记录出现的次数
            ans[tuple(count)].append(s)
        return ans.values()

nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(nums))

