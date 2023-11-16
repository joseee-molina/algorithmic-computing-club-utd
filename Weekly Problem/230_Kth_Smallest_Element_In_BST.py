# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

algo = '''

    clarification questions: 
    - what if they give a k greater than the size
    of the tree?
    - what if the root is None
    - can k be negative? (getting the largest values vs the smallest ones)


         9
       /   \ 
      7     10
     / \      \
    4   8      12 
      \
       6
      /
     5

     

    if k = 1 --> return the ( leftmost ) node
    if k = 2 --> return the ( leftmost.right.leftmost ) node
    
    Remark: dfs will always take us to the leftmost node
    
    Solution: start dfs at root, whenever we get to the leftmost, 
    do k-=1, if k!=0, get leftmost of root.right subtree and do k-=1 again

    Remark: only do k-=1 when we finished exploring left as much as we could



 '''


class Solution(object):
    index = 0
    ans = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.index = k
        self.dfs(root)
        return self.ans.val
        
    def dfs(self, root):
        if root == None:
            return

        self.dfs(root.left)

        self.index-=1
        if self.index == 0:
            self.ans = root
        
        self.dfs(root.right)
        