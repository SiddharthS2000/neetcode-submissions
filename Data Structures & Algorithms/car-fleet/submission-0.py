class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        time_stack = []
        for p, s in sorted(pair)[::-1]:
            time_stack.append((target - p) / s)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
        return len(time_stack)