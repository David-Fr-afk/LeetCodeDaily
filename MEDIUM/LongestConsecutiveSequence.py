class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        sorted_nums = sorted(num_set)
        i = sorted_nums[0]
        streak = 0
        longest = 0
        for j in range(0, len(sorted_nums)):
            if sorted_nums[j] == i:
                i += 1
                streak +=1
            else:
                longest = max(longest, streak)
                i = sorted_nums[j] + 1
                streak = 1
        longest = max(longest, streak)
        return longest
    
    ##Above is the solution i created and designed. This is in O(nlogn) which is pretty slow so below ill attach the faster method which is in O(n)
    # After testing on leetcode, My solution is actually faster because using sorted is more efficent. I still prefer the solution on the bottom as it is overall less complex. But if were going for pure speed and efficeny my code wins.
    def longestConsecutive(self, nums):
        num_set = set(nums)
        streak = 0
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set:
                current = num
                streak = 1
                while (current + 1) in num_set:
                    streak += 1
                    current += 1
            longest = max(longest, streak)
        return longest
        # this in my opinion is the easier to understand solution. You just need to know how sets work in python. Overall i liked coding this problem.