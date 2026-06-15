from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
        return result[::-1]
