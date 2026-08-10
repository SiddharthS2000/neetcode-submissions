class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], idx]
            prev_map[num] = idx

        return []