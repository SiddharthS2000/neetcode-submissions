class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(float(i) / mid)

            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res