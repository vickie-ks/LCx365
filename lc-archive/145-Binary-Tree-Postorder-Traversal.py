from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)
        traverse(root)
        return result

node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(2)

node1.left = node2
node1.right = node3

sol = Solution()
result = sol.postorderTraversal(node1)
print(result)