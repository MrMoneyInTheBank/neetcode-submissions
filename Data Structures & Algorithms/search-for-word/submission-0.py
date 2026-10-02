class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()

        def dfs(row: int, col: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if row not in range(len(board)):
                return False
            if col not in range(len(board[0])):
                return False
            if board[row][col] != word[idx]:
                return False
            if (row, col) in seen:
                return False
            
            seen.add((row, col))
            one = dfs(row + 1, col, idx + 1)
            two = dfs(row - 1, col, idx + 1)
            three = dfs(row, col + 1, idx + 1)
            four = dfs(row, col - 1, idx + 1)
            seen.remove((row, col))
        
            return one or two or three or four
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        
        return False
        