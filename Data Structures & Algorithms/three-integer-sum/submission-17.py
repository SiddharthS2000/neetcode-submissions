class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, first in enumerate(nums):
            if idx > 0 and  first == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                threesum = first + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    res.append([first, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left< right:
                        left += 1

        return res












        # res = []
        # nums.sort()

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]:
        #         continue

        #     l, r = i+1, len(nums) - 1
        #     while l < r:
        #         threesum = a + nums[l] + nums[r]
        #         if threesum > 0:
        #             r -= 1
        #         elif threesum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
        # return res
