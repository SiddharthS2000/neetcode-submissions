class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        left_pointer, right_pointer = 0, len(height) - 1
        left_max_height, right_max_height = height[left_pointer], height[right_pointer]

        while left_pointer < right_pointer:
            if left_max_height < right_max_height:
                left_pointer += 1
                left_max_height = max(height[left_pointer], left_max_height)
                water += left_max_height - height[left_pointer]

            else:
                right_pointer -= 1
                right_max_height = max(height[right_pointer], right_max_height)
                water += right_max_height - height[right_pointer]

        return water
                

            






