class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                top_index, top_temp = stack.pop()
                res[top_index] = idx - top_index
            stack.append((idx, temp))


        return res


