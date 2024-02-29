from typing import List
from collections import deque

# read pdf writeup first to help understand the approach used here

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # current sum of f(j)
        res = 0
        stack = deque()

        # enumerate lists pairs of the form (i, arr[i])
        for j, x in enumerate(arr):

            # pop all invalid n_j
            while stack and arr[stack[-1][0]] > x:
                stack.pop()

            if stack:
                # i = n_j, s = f(n_j)
                i, s = stack[-1]

                # ns = f(j) = f(n_j) + (j - n_j) * A[j]
                ns = (s + (j - i) * x)
            else:
                # ns = f(j) = (j + 1) * A[j]
                ns = ((j + 1) * x)

            # keep numbers small
            ns %= MOD

            # add f(j) to overall sum
            res = (res + ns) % MOD

            # push j, f(j) onto stack
            stack.append((j, ns))
        
        return res
