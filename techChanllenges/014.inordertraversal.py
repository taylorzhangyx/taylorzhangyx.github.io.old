# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = deque()

        def pushleft(node):
            while node:
                stack.append(node)
                node = node.left

        cur = root

        while True:
            pushleft(cur)
            if not len(stack):
                return res
            node = stack.pop()
            res.append(node.val)
            cur = node.right
