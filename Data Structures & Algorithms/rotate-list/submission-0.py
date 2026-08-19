# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        leng = 1
        tail = head

        while tail.next is not None:
            tail = tail.next
            leng += 1

        tail.next = head

        k = k % leng

        steps = leng - k
        newTail = head
        for _ in range(steps - 1):
            newTail = newTail.next

        newHead = newTail.next

        newTail.next = None

        return newHead

        