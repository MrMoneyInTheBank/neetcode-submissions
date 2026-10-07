class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: dict[int, set[int]] = {i: set() for i in range(9)}
        cols: dict[int, set[int]] = {i: set() for i in range(9)}
        boxes: dict[tuple[int, int], set[int]] = {
            (i, j): set() for i in range(3) for j in range(3)
        }
    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rows[row]:
                    return False
                elif board[row][col] in cols[col]:
                    return False
                elif board[row][col] in boxes[(row // 3, col // 3)]:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3, col // 3)].add(board[row][col])
        
        return True
        