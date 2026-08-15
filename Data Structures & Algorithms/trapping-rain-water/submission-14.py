class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        left_ptr = 0
        right_ptr = len(height) - 1

        maxheightleft = height[left_ptr]
        maxheightright = height[right_ptr]

        while left_ptr < right_ptr:
            if maxheightleft < maxheightright:
                left_ptr += 1
                maxheightleft = max(maxheightleft, height[left_ptr])
                res += maxheightleft - height[left_ptr]

            else:
                right_ptr -= 1
                maxheightright = max(maxheightright, height[right_ptr])
                res += maxheightright - height[right_ptr]

        return res