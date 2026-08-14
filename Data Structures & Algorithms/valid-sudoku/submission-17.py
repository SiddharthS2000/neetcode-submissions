class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_record = defaultdict(set)
        col_record = defaultdict(set)
        subtable_record = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_record[r] or board[r][c] in col_record[c] or board[r][c] in subtable_record[(r//3, c//3)]:
                    return False
            
                row_record[r].add(board[r][c])
                col_record[c].add(board[r][c])
                subtable_record[(r//3, c//3)].add(board[r][c])

        return True



        