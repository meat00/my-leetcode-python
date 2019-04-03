#!env python3

class Solution:
    def twoSum(self, nums, target):
        m = dict()
        for i,n in enumerate(nums):
            ret = target - n
            # 注意这里需要判断!=None,因为get(ret)可能返回0
            if m.get(ret) != None:
                return [i, m[ret]]
            m[n] = i

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = s.twoSum(nums, target)
    print(result)
