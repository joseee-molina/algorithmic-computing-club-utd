/*
In this question we essentially want to see how many groups of the number 1 exist in the grid. If 1's are touching they count as one group.

The first thing that I did was create a variable (ans) that will be used to count the number of groups of 1s that exist inside of our grid.

Then I created a nested for loop. The outermost for-loop is used to traverse through each of the rows in the grid (so that means the variable i represents the row that we are currently visiting). The inner for-loop represents the column that we are visiting (so j is the current column).
We want to traverse through each element of the array and if we find a 1 that means that we have discovered a new group, so we increment the counter (ans) and then call the DFS function that will be changing that 1 and all of the other 1's that are touching it into 0s. We want to convert them to 0s because we have already counted this group, and changing them to 0s will prevent us from accidentally counting them again.

To solve this question I created a DFS function (public void DFS), and it takes in 3 parameters: the grid (char[][] grid), the current row (i), and the current column (j). 


Inside of this DFS function we first check to see if the arguments that we are passing to it will go out of bounds. i represents the row that we are currently visiting inside of the matrix, so if we go below 0 or if we go above the maximum number of rows (grid.length-1) we will be outside of the boundaries. We do the same for the columns (j). If our value for j is 0 or it is greater than grid[0].length-1 (grid[0].length-1 is the last array index of each row), then we know that we are out of bounds and need to exit. 

After checking to ensure that the function will not be going out of bounds we want to see if we are visiting a 1, if it isn't a 1 then we want to return as we are trying to find all the 1s that are touching. 

^That if statement is essentially the base case for this recursively calling function. Once we pass that we then move on and first change the current index (which should be a 1) into a 0, and then we want to change all of the other 1s that are touching it into 0.

The question states that we only want to check if they are touching horizontally or vertically, so we call the recursively call the DFS function by going up 1 index, down 1 index, left 1 index, right 1 index of the current index. If any of those are out of bounds or aren't a 1 then our base case will return and won't change them. If they are a 1 though we essentially do what we did before, and keep repeating the process. Because the function recursively calls itself it can keep spreading and changing all 1s that are touching it into 0s.

Once all of the 1s that were touching the 1 that initially caused us to call the DFS function have been changed to 0s we return back to the nested for loops and keep traversing through the grid. If we find any other 1s we will increment the counter (ans) again, then call the DFS function again to convert all of the 1s touching it into 0s. We keep repeating this process until all of elements in the grid have been visited.

This solution is great because you are directly modifying the grid, so you don't have to track which indexes have already been visited. For example say if our first row is all 1s, when we visit the first element of the row we will call our function and that will change the row to all 0s. Then as we continue to go through each element of the grid our function won't try calling on those 1s again since they are already 0s, which is why we don't have to worry about if the indices have already been visited. This reduces the space complexity because you don't have to use a set to track if the indices have already been visited or not.

*/

class Solution {
    public int numIslands(char[][] grid) {
        int ans = 0;
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == '1') {
                    ans++;
                    DFS(grid, i, j);
                }
            }
        }
        return ans;
    }

    public void DFS(char[][] grid, int i, int j) {
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != '1') {
            return;
        }
        grid[i][j] = '0';
        DFS(grid, i, j+1);
        DFS(grid, i, j-1);
        DFS(grid, i+1, j);
        DFS(grid, i-1, j);
        return;
    }
}
