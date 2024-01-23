/* In this problem we are starting at the first index of an array and are trying to determine if we can make it to the array's last index. WThe number at each array index represents how many spaces that you can move forward if you visit them. 

I solved this question using a greedy algorithm approach. I first created an integer variable that I called max to represent the current farthest distance that we can jump. I then created a for loop starting at index 0 (the first index of the array) and ending at the last index of the array (nums.length). First inside of the for loop I had an if statement to check if i was greater than the current value stored in max. If i is greater than max that means we are traying to  jump to the right of the array, but since it is greater than max we are trying to jump farther than the maximum jump distance which is impossible, so here we would return false.

Assuming that we don't return false there though, we check to see if we need to update the max distance. I used java's Math.max method to compare the current value of max to whatever index we are visitng+the value stored inside of it (i+nums[i]). This way if it is possible for us to jump farther than what is currently stored as the maximum, we can update the max variable. 

Once all elements have been traversed we check to see if the value of max is >= the length of the array. 

*/

class Solution {
    public boolean canJump(int[] nums) {
        int max = 0;
        for(int i = 0; i < nums.length; i++) {
            if(i > max) return false;
            max = Math.max(max, i+nums[i]);
        }
        return max >= nums.length-1;
}
}
