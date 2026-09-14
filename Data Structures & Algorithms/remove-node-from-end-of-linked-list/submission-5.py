# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        i = 0

        if not head.next:
            return None

        while(head):
            head = head.next
            i += 1

        index = i - n - 1
        ans = prev
        while(index > 0):
            prev = prev.next
            index -= 1

        print(prev.val, prev.next.val)

        if i == n:
            return prev.next

        if not prev.next:
            prev.next = None
            return ans

        prev.next = prev.next.next
        return ans
        # prev is the one before delete


            


        

        