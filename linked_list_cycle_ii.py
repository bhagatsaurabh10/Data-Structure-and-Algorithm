from typing import Optional

class Solution:
    def detectCycle(self, head: Optional['ListNode']) -> Optional['ListNode']:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                finder = head
                while finder is not slow:
                    finder = finder.next
                    slow = slow.next
                return finder
        return None
