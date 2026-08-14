class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(area, max_area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            
        return max_area





















        # max_vol = 0
        # l, r = 0, len(heights) - 1
        # while l < r:
        #     min_height = min(heights[l], heights[r])
        #     vol = min_height * (r - l)
        #     max_vol = max(max_vol, vol)
            
        #     if heights[r] < heights[l]:
        #         r -= 1
        #     else:
        #         l += 1

        # return max_vol