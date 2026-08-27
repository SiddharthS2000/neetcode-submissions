class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0    
        # res = 0

        # leftmax, rightmax = 0,0
        # leftmax_array, rightmax_array, min_array = [0]*len(height), [0]*len(height), [0]*len(height)
        
        # for i in range(len(height)):
        #     leftmax_array[i] = max(height[i], leftmax)
        #     leftmax = leftmax_array[i]

        # for i in range(len(height) - 1, -1, -1):
        #     rightmax_array[i] = max(height[i], rightmax)
        #     rightmax = rightmax_array[i]

        # for i in range(len(height)):
        #     min_array[i] = min(rightmax_array[i], leftmax_array[i])
        #     if min_array[i] > height[i]:
        #         res += min_array[i] - height[i]

        # return res



        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        water = 0
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(height[left], maxLeft)
                water += maxLeft - height[left]

            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                water += maxRight - height[right]

        return water
