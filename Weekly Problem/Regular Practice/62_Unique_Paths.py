class Solution(object):
    grid = []
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.grid = [[0]*n for _ in range(m)]
        self.grid[m-1][n-1] = 1
        self.paths(0,0)
        return self.grid[0][0]
        
    
    def paths(self,x,y):
        if x>=len(self.grid) or y>=len(self.grid[0]):
            return 0

        if self.grid[x][y] == 0:
            self.grid[x][y] = self.paths(x+1,y) + self.paths(x,y+1)
        
        return self.grid[x][y] 

#uncomment these if testing in VSC
#example = Solution()
#print(example.uniquePaths(3,7))