from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional['ListNode'], left: int, right: int) -> Optional['ListNode']:
        dummy = ListNode(0, head)
        before = dummy
        for _ in range(left - 1):
            before = before.next
        prev = None
        current = before.next
        for _ in range(right - left + 1):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        tail = before.next
        before.next = prev
        tail.next = current
        return dummy.next
