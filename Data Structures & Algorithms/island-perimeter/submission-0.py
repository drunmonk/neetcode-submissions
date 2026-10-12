class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        visted=set()
        s=0
        x=len(grid)
        y=len(grid[0])

        def dfs(i,j):
                    nonlocal s
                    
                    visted.add((i,j))

                    sides=[(i,j+1),(i,j-1),(i-1,j),(i+1,j)]
                    for k,m in sides:
                        if not (0<=k<x and 0<=m<y):
                            s+=1
                        elif grid[k][m]==0:
                            s+=1
                        elif (k,m) not in visted:
                            dfs(k,m)
                    
                    return 
        

        for i in range(x):
            for j in range(y):
                if grid[i][j]and (i, j) not in visted:
                    dfs(i,j)

        return s
            


        




                


        