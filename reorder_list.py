from typing import Optional

class Solution:
    def reorderList(self, head: Optional['ListNode']) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first, second = head, prev
        while second:
            f_next = first.next
            s_next = second.next
            first.next = second
            second.next = f_next
            first = f_next
            second = s_next
