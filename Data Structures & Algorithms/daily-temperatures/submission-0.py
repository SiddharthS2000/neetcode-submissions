class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = (idx - stackIndex)
            stack.append([idx, temp])

        return res
            
