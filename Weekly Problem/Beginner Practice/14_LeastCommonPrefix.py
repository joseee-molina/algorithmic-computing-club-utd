class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        lcp = strs[0]
        for j in range(len(lcp), -1, -1):
            if strs[-1][:j] == lcp[:j]:
                return lcp[:j]
        return ""
