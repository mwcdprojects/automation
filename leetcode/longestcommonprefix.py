class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = []
        a = iter([each for each in strs])
        max = ""
        while len(strs!=0):
            i = 0
            j=i+1


        res = list(reduce(lambda j,i: j & i, (set(x) for x in strs)))
        # for positem in enumerate(strs):
        #     if strs[pos][pos]==strs[pos+1][pos]:
        #         max = strs[pos][pos]
        print res
        # first = a.next()
        # second = a.next()
        # for pos,i in enumerate(strs):
        #     for j in range(len(i)):
        #         if strs[pos][j] == strs[pos+1][j]:
        #             l.append(i[j])
        #print max
        # for item in strs:
        #     for i in range(len(strs)):
        #
        #         if a.next()[i] == a.next()[i]:
        #             l.append()

if __name__ == '__main__':
    Solution().longestCommonPrefix(["dog", "racecar", "car"])
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
