class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row not in range(len(grid)):
                return
            elif col not in range(len(grid[0])):
                return
            elif grid[row][col] != "1":
                return
            
            grid[row][col] = "x"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
        
        return res