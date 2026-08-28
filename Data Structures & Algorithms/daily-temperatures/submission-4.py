class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                top_ind, top_temp = stack.pop()
                res[top_ind] = idx - top_ind
            stack.append([idx, temp])
        return res