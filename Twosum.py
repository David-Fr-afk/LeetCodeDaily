class Solution(object):
    def twoSum(self, nums, target):
        int_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return None
