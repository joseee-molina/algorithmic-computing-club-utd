class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        algo = '''
                                 
            haystack = asadbutsad     
            needle =          sad
            haystack[0:3] = asa
            haystack[1:4] = sad

        '''

        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
    
    #uncomment if running in vsc for testing
    #print(strStr("", "asadsad", "sad"))