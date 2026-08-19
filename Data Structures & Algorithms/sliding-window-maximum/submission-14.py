from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], window_size: int) -> List[int]:
        """
        Compute the maximum value in each sliding window of size `window_size` 
        across the list `nums`.

        Args:
            nums (List[int]): The input list of integers.
            window_size (int): The size of the sliding window.

        Returns:
            List[int]: A list containing the maximum value from each window.

        Approach:
            - Use a deque to store indices of elements that are potential maximums.
            - Maintain the deque in decreasing order of values (front = largest).
            - Remove indices that fall outside the current window.
            - Once the window reaches size `window_size`, record the maximum.
        """
        result = []
        index_deque = deque()

        left_pointer, right_pointer = 0, 0
        
        while right_pointer < len(nums):
            # Remove smaller values from the deque (they can't be maximums)
            while index_deque and nums[index_deque[-1]] < nums[right_pointer]:
                index_deque.pop()

            # Add current index to deque
            index_deque.append(right_pointer)

            # Remove leftmost index if it's outside the current window
            if left_pointer > index_deque[0]:
                index_deque.popleft()

            # Once window size is reached, record the maximum
            if right_pointer + 1 >= window_size:
                result.append(nums[index_deque[0]])  # Front of deque = max
                left_pointer += 1                    # Slide window forward

            # Expand window to the right
            right_pointer += 1

        return result


