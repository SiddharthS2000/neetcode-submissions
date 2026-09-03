from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_length = m + n
        half = total_length // 2

        left, right = 0, m - 1
        while True:
            # Partition index for nums1
            partition1 = (left + right) // 2
            # Partition index for nums2 is derived so that left side has 'half' elements
            partition2 = half - partition1 - 2

            # Get boundary values around the partitions
            left1 = nums1[partition1] if partition1 >= 0 else float("-inf")
            right1 = nums1[partition1 + 1] if (partition1 + 1) < m else float("inf")
            left2 = nums2[partition2] if partition2 >= 0 else float("-inf")
            right2 = nums2[partition2 + 1] if (partition2 + 1) < n else float("inf")

            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                if total_length % 2:  # Odd total length
                    return min(right1, right2)
                # Even total length
                return (max(left1, left2) + min(right1, right2)) / 2

            # Adjust search range
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1
