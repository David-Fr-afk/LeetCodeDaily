class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        sorted_nums = sorted(num_set)
        i = sorted_nums[0]
        streak = 0
        for j in range(0, len(sorted_nums)):
            if sorted_nums[j] == i:
                i = i + 1
        return i
                        
                        





        """
        :type nums: List[int]
        :rtype: int
        """
        