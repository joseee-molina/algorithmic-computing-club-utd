class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        fullset = {} # Dict K: a char, V: the set it belongs to
        dex = 0 # the next available set index, gets inc. every time a new set is required

        def searchAndMin(element):
            if element not in fullset:
                return element # no possible replacement, so return as is
            else:
                return min([x for x in fullset if fullset[x]==fullset[element]]) # find minim of same set

        def searchAndAdd(element, companion):
            fullset[element] = fullset[companion] # they belong to the same set

        def merge(e1, e2):
            s1 = fullset[e1] # set 1
            s2 = fullset[e2] # set 2
            
            if s1 != s2:
                superset = [x for x in fullset if fullset[x]==s1 or fullset[x]==s2] # union of sets 1 and 2
                for s in superset:
                    fullset[s] = dex # put them all in a new set
                return True # if merge happened
            return False # if merge did not happen
            
        for i in range(len(s1)):
            a = s1[i]
            b = s2[i]
            if a == b:
                if a not in fullset: # if it's new, otherwise no need to change anything
                    fullset[a] = dex
                    dex += 1
            else:
                if a not in fullset and b not in fullset: # both need to be put in a new set together
                    fullset[a], fullset[b] = dex, dex
                    dex +=1 
                elif a not in fullset: # b exists, so add a to it
                    searchAndAdd(a, b)
                elif b not in fullset: # a exists, so add b to it
                    searchAndAdd(b, a)
                elif a and b in fullset: # both exist, so check if merge required
                    if merge(a, b): # if merged, they got added to dex, so we must inc. for future
                        dex += 1

        res = ""
        for i in baseStr:
            res += searchAndMin(i) # get smallest possible char 
        return res
