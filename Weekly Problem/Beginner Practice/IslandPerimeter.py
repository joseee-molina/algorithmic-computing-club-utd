class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # going to need to find what is next to each other
        # depending on how many they touch it impacts their number of sides counting
        # could we code this to be determined by the number of touching points
        # one connection - 3 sides
        # two connections - 2 sides
        # three connections - 1 side
        # four connections - 0 sides
        perimeter = 0

        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter = perimeter - 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter = perimeter - 2
        
        return perimeter