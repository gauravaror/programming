# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        temp = None
        rem = 0
        while (l1 or l2 or rem !=0):
            val = rem
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val > 9:
                rem = val //10
                val = val % 10
            else:
                rem = 0
            if not head:
                head = ListNode(val)
                temp = head
            else:
                temp.next = ListNode(val)
                temp = temp.next
        return head
