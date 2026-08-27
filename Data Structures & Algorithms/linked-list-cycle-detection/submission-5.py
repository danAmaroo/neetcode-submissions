# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast, slow = head.next, head
        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
