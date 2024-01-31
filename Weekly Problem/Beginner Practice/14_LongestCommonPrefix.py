class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        common prefix for all strings
        strs[0] = "flower"

        i = 0
        "f lower", "f low", "f light"
        res = "f"

        i = 1
        "fl ower, "fl ow, "fl ight"
        res = "fl"

        i = ...
        '''
        res = ''
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or strs[0][i] != word[i]:
                    return res
            res += word[i]
        return res
    
    #uncomment if running in vsc for testing
    #print(longestCommonPrefix("", ["flower","flow","flight"]))