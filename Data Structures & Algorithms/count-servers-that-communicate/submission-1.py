class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        x= len(grid)
        y=len(grid[0])
        row_cont=[0]*x
        col_count=[0]*y

        for r in range(x):
            for c in range(y):
                if grid[r][c]==1:
                    row_cont[r]+=1
                    col_count[c]+=1
        res=0

        for r in range(x):
            for c in range(y):
                if grid[r][c] and max(row_cont[r],col_count[c])>1:
                    res+=1
        return res



        


