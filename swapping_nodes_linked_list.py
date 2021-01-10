# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        siphon = ListNode(0, head)
        slow = siphon
        fast = siphon
        while k > 0:
            if k == 1:
                firstback =  fast
            fast = fast.next
            k -= 1
        if not fast:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        #print(firstback, slow)
        front_elem = firstback.next
        back_elem = slow.next
        if front_elem == back_elem:
            return head
        firstback.next, slow.next = slow.next, firstback.next
        front_elem.next, back_elem.next = back_elem.next, front_elem.next
        return siphon.next
        
            
        
