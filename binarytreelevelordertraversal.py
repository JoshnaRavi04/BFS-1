# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time Complexity: O(n)
# Space Complexity: O(h)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        self.result = []

        def helper(root, level):
            if not root:
                return

            if len(self.result) == level:
                self.result.append([])

            self.result[level].append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        helper(root, 0)
        return self.result