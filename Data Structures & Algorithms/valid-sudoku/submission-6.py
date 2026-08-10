class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subtables = defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue
                
                if (
                    board[row][column] in rows[row] or 
                    board[row][column] in columns[column] or 
                    board[row][column] in subtables[(row // 3, column // 3)]
                ):
                    return False
                
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                subtables[(row//3, column//3)].add(board[row][column])
        return True
        