class Solution(object):
    def containsDuplicate(self, nums):
        int_map = {}
        for num in nums:
            int_map[num] = int_map.get(num, 0) + 1
            if int_map[num] > 1:
                return True
        return False
#this was easy as i could base it on the previous leetcode question i did called "ValidAnagram"