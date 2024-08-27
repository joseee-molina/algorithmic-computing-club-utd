class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)==1:
            return False
        nums = [int(x%k) for x in nums]
        dx = {}
        mod = 0
        dx[0] = 0
        ctr = 1
        for x in nums:
            mod = int((x+mod)%k)
            if mod not in dx:
                dx[mod] = ctr
            else:
                if ctr - dx[mod] > 1:
                    return True
            ctr += 1
        return False
