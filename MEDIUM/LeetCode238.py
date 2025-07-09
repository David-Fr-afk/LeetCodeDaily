class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return ""
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
  
        