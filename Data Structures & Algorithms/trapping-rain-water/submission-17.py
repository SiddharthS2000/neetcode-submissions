class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0    
        res = 0
        
        left, right = 0, len(height) - 1
        leftmax, rightmax = height[left], height[right]
        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                res += leftmax - height[left]

            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                res += rightmax - height[right]

        return res



















        # res = 0
        # left_ptr = 0
        # right_ptr = len(height) - 1

        # maxheightleft = height[left_ptr]
        # maxheightright = height[right_ptr]

        # while left_ptr < right_ptr:
        #     if maxheightleft < maxheightright:
        #         left_ptr += 1
        #         maxheightleft = max(maxheightleft, height[left_ptr])
        #         res += maxheightleft - height[left_ptr]

        #     else:
        #         right_ptr -= 1
        #         maxheightright = max(maxheightright, height[right_ptr])
        #         res += maxheightright - height[right_ptr]

        # return res