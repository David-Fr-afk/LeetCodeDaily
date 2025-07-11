class Solution(object):
    def topKFrequent(self, nums, k):
        freqmap = {}

        # Count frequencies
        for num in nums:
            if num in freqmap:
                freqmap[num] += 1
            else:
                freqmap[num] = 1

        sorted_items = sorted(freqmap.items(), key=lambda item: item[1], reverse=True)
        top_k_keys = [key for key, value in sorted_items[:k]]
        return top_k_keys





