# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# S1, in place visit
# Note:
# 1. reconstruct the linked list in-place requires pass in the start and end index of the 2 orders to make the recursion successful.
# 2. The index passed in need to be valid index or a error will throw due to the invalid index.
# 3. It doesn't matter which node the recusion will first access to. Since it does not modify the original list.
class Solution1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        # preprocess the inorder list
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        return self.buildTreeNode(
            inorder, postorder, dic, 0, len(postorder) - 1, 0, len(postorder) - 1
        )

    def buildTreeNode(self, inorder, postorder, dic, in_l, in_r, po_l, po_r):
        # end condition
        if in_l > in_r or po_l > po_r:
            return None

        # process
        root = postorder[po_r]
        rootNode = TreeNode(val=root)
        i = dic[root]
        rootNode.left = self.buildTreeNode(
            inorder, postorder, dic, in_l, i - 1, po_l, po_l + (i - in_l) - 1
        )
        rootNode.right = self.buildTreeNode(
            inorder, postorder, dic, i + 1, in_r, po_l + (i - in_l), po_r - 1
        )

        return rootNode
