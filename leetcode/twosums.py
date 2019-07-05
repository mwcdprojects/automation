from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):

        d = {}
        a = []
        for pos, i in enumerate(nums):
            #d[(pos)] = i
            for j in range(1,len(nums)):
                if i + nums[j] == target and pos != j:
                    return ([pos,j])

        # for k,v in d.iteritems():
        #
        #
        #
        #
        # for each in nums:
        #     if target - each in nums and each == target - each and len(nums)==2 and nums.index(each) not in a:
        #         a.append([d[each, nums.index(each)], d[target - each, nums.index(target - each) + 1]])
        #         break
        #     elif target-each in nums and nums.index(each) not in a and nums.index(target-each) not in a:
        #         a.append([d[each, nums.index(each)], d[target - each, nums.index(target - each)]])
        #         break
        #         #return ([d[each, nums.index(each)], d[target - each, nums.index(target - each) + 1]])
            # elif target - each in nums and each == target - each and len(nums)>2:
            #     return ([d[each, nums.index(each)], d[target - each, nums.index(target - each) + 1]])
            # elif target-each in nums and each != target-each:
            #     return ([d[each, nums.index(each)], d[target - each, nums.index(target - each)]])
        #return a

if __name__ == "__main__":
    x = Solution()
    print (x.twoSum([3, 3], 6))
    print (x.twoSum([2, 1, 4, 5], 9))
    print (x.twoSum([2, 7, 11, 15], 9))
    print (x.twoSum([3, 2, 4], 6))
    print (x.twoSum([3,2,3],6))
    print (x.twoSum([2,5,5,11],10))