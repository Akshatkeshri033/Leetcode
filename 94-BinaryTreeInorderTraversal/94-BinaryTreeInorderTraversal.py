# Last updated: 8/20/2025, 5:49:29 PM
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)     # left
            result.append(node.val)  # root
            inorder(node.right)    # right

        inorder(root)
        return result
