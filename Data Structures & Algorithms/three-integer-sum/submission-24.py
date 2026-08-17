class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for idx, first in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                sum = first + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([first, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
















        # res = []
        # nums.sort()
        # for idx, first in enumerate(nums):
        #     if idx > 0 and first == nums[idx - 1]:
        #         continue
        #     left = idx + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         threesum = first + nums[left] + nums[right]
        #         if threesum < 0:
        #             left += 1
        #         elif threesum > 0:
        #             right -= 1
        #         else:
        #             res.append([first, nums[left], nums[right]])
        #             left +=1
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1

        # return res





