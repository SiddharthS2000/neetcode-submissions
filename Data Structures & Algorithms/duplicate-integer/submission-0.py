class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracking_set = set()
        for num in nums:
            if num in tracking_set:
                return True
            tracking_set.add(num)
        return False