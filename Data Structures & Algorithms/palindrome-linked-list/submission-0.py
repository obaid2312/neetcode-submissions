# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        s = head
        f = head

        while f is not None and f.next is not None:
            s = s.next
            f = f.next.next

        prev = None
        front = None

        while s is not None:
            front = s.next
            s.next = prev
            prev = s
            s = front

        while prev is not None:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next
        return True
        