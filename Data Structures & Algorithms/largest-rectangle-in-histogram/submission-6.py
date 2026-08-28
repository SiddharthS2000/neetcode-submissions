class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0


        for i, h in enumerate(heights):
            start_index = i
            while stack and stack[-1][1] > h:
                top_index, top_height = stack.pop()
                max_area = max(max_area, top_height * (i - top_index))
                start_index = top_index
            stack.append((start_index, h))


        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))


        return max_area

        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         top_index, top_height = stack.pop()
        #         max_area = max(max_area, top_height * (i - top_index))
        #         start = top_index
        #     stack.append((start, h))

        # for i, h in stack:
        #     max_area = max(max_area, h * (len(heights) - i))

        # return max_area