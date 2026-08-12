class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            area = 1
            q = deque([[r, c]])
            while q:
                directions = [[0,1], [0, -1], [1, 0], [-1,0]]
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1 and (row, col) not in visit:
                        visit.add((row,col))
                        q.append([row,col])
                        area += 1
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    visit.add((r, c))
                    area = bfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area




        # rows, columns = len(grid), len(grid[0])
        # visited = set()
        # max_area = 0

        # def bfs(row, column):
        #     area = 1
        #     q = deque([[row,column]])
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0], [-1,0], [0,1], [0, -1]]

        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (
        #                 r in range(rows) and 
        #                 c in range(columns) and 
        #                 grid[r][c] == 1 and 
        #                 (r, c) not in visited
        #                 ):
        #                 q.append([r,c])
        #                 visited.add((r, c))
        #                 area += 1
        #     return area

        # for row in range(rows):
        #     for column in range(columns):
        #         if grid[row][column] == 1 and (row, column) not in visited:
        #             visited.add((row, column))
        #             area = bfs(row, column)
        #             max_area = max(area, max_area)
        # return max_area