class Solution:
    def majorityElement(self, nums):
        '''
        Refer to Boyer-Moore Majority Voting Algorithm
        O(n) time and O(1) space
        
        '''
        candidate =  nums[0]
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num

            if candidate == num:
                counter += 1
            else:
                counter -= 1

        return candidate
'''
class Solution:
    # Hashmap Solution
    # Maps count of each element then returns the one with a count greeater than n // 2 of the list

    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            if value > len(nums) // 2:
                return key
'''
# Uncomment if running on VSC
# sol = Solution()
# print(sol.majorityElement([2,2,1,1,1,2,2]))