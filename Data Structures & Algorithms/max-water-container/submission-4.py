class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(heights) - 1
        while l < r:
            min_height = heights[l] if heights[l] < heights[r] else heights[r]
            vol = min_height * (r - l)
            if vol > max_vol:
                max_vol = vol
            
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max_vol