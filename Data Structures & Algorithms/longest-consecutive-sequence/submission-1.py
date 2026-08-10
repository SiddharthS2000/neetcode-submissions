class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for n in nums:
            if n - 1 in nums:
                continue
            
            length = 1
            while n + length in nums:
                length += 1
            
            max_len = max(max_len, length)
        return max_len
