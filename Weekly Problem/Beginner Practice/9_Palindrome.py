class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        algo = '''

            x = 12321
            
            (convert to string)

            initially (i = 0, j = len-1)

            x = "1 2 3 2 1"
                 i
                         j
            
            check if x[i] != x[j]
            
            move i right, and j left

            x = "1 2 3 2 1"
                   i
                       j

        '''

        x = str(x)
        i = 0
        j = len(x)-1

        while i<j:
            if x[i]!=x[j]:
                return False
            i+=1
            j-=1

        return True 