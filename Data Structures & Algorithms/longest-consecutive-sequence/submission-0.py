class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)
        for n in num_set:
            if (n-1) in num_set:
                continue

            length = 1
            while (n + length) in num_set:
                length += 1
            
            max_length = max(max_length, length)
        return max_length