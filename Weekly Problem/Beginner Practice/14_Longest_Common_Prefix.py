class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ideas = '''
        strs = 
            [ flower ,
            flow ,
            flight 
            ]

            prefix = "flower" -> "flow" -> "fl"

        '''

        prefix = strs[0]

        for x in strs:
            i = 0
            while i<len(prefix) and i<len(x) and (prefix[i] == x[i]):
                i+=1
            prefix = prefix[0:i]

        return prefix
    
# Uncomment if running on VSC
# sol = Solution()
# print(sol.longestCommonPrefix(["flower", "flow", "flight"]))