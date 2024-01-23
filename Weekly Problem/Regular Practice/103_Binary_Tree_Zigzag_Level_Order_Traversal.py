# 
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#       Basic example
#
#                   3
#                 /   \
#               9       20
#                      /  \
#                     15   7
#                   
#
#       3, 20 9, 15 7
#
#       Clarifying questions: can we be passed an empty tree?
#       Yes -> null
#
#       Is there a maximum number of nodes? 2,000 
#       
#       Algorithm:
#
#       
#                   3
#                 /   \
#               9       20
#             /  \      /  \
#           11    2    15   7
#              \
#                4
#
#       ans = []
#
#       queue of nodes to visit = [3]
#
#       ans = [[3]]
#
#       children of 3: [9,20]
#
#       ans = [[3],[20,9], [11,2,15,7], [4]] 
#
#       queue of nodes to visit = children of curr level = [9,20]
#
#       --> return ans
#
#       TC: N where N is the number of nodes
#       SC: worst case N, and tree is balanced height of k = log(N) -> 2^k ---> N SC
#

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        ans = []

        queue = [root]

        ans.append([root.val])
        leftToRight = False

        while queue:
            children = []
            for el in queue:
                if el.left:
                    children.append(el.left)
                if el.right:
                    children.append(el.right)
            
            if not leftToRight:
                ans.append([x.val for x in children[::-1]])
                leftToRight = not leftToRight
            else:
                ans.append([x.val for x in children])
                leftToRight = not leftToRight

            
            queue = children
        
        if ans[-1] == []:
            ans.pop()
        return ans


