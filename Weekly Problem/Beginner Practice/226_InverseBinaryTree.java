/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        Queue<TreeNode> q = new LinkedList<>();
        TreeNode iter = root;
        q.add(iter);
        while(!q.isEmpty()){ //For every new node, swap its children
            iter = q.poll();
            if(iter.left != null)
                q.add(iter.left);
            if(iter.right != null)
                q.add(iter.right);

            TreeNode temp = iter.right;
            iter.right = iter.left;
            iter.left = temp;
        }
        return root;
    }
}