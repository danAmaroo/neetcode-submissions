# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_sum = ""
        l2_sum = ""

        while(l1):
            l1_sum += str(l1.val)
            l1 = l1.next

        while(l2):
            l2_sum += str(l2.val)
            l2 = l2.next

        total = str(int(l1_sum[::-1]) + int(l2_sum[::-1]))
        total = total[::-1]
        
        
        head = ListNode()
        prev = head

        for i in range(len(total)):
            if i == 0:
                head.val = int(total[i])
                continue

            tmp = ListNode(int(total[i]), None)
            prev.next = tmp
            prev = tmp

        return head


        