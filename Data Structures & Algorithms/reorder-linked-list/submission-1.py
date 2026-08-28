# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointers to find middle
        # reverse second half
        # insert second half into first

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # second half
        slow.next = prev = None

        # 2, 4, 6, 8
        # 2->4->None 6->8->None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 2->4->None None<-6<-8
        # head                 second
        second = prev

        while head and second:
            temp = head.next
            temp1 = second.next
            head.next = second
            second.next = temp
            head = temp
            second = temp1


        


    

        
        

        