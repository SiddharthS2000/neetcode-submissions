class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        q = deque()

        def addRoom(r, c):
            if r < 0 or c < 0 or c == COLS or r == ROWS or (r, c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            q.append([r,c])

        for r_index in range(ROWS):
            for c_index in range(COLS):
                if grid[r_index][c_index] == 0:
                    visit.add((r_index, c_index))
                    q.append([r_index, c_index])

        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)      

            dist += 1
