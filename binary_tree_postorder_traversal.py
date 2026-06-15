from typing import List, Optional

class Solution:
    def postorderTraversal(self, root: Optional['TreeNode']) -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
