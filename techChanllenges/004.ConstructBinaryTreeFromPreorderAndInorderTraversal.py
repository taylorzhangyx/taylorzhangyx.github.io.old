# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Note
# Similar to 003, this is using the deque class from package to achieve the queue.
# This recursive solution is highly impacted by the order of the nodes to be constructed that is the left node is always constructed before the right one.

from collections import deque


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # corner case check
        preL = len(preorder)
        inL = len(inorder)
        if preL == 0 or inL == 0 or preL != inL:
            return None

        # copy to void modifying the original instance
        listPre = deque(preorder)
        listIn = deque(inorder)

        # prepare the dic
        dic = {}
        for i in range(preL):
            dic[inorder[i]] = i

        # recursion
        def buildTreeNode(l, r):
            if l > r:
                return None

            head = TreeNode(listPre.popleft())
            i = dic[head.val]
            head.left = buildTreeNode(l, i - 1)
            head.right = buildTreeNode(i + 1, r)
            return head

        return buildTreeNode(0, preL - 1)
