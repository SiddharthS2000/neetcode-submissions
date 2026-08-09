class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            diff = target - nums[idx]
            if diff in nums and nums.index(diff) != idx:
                return sorted([nums.index(diff), idx]) 

        return []