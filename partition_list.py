# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pivot = ListNode(-1000)
        pivot.next = head
        small_end = elem = pivot
        while True:
            if elem and elem.next and elem.next.val < x:
                tmp = elem.next
                elem.next = elem.next.next
                tmp2 = small_end.next
                small_end.next = tmp
                small_end.next.next = tmp2
                if small_end == elem:
                    small_end = small_end.next
                    elem = elem.next
                else:
                    small_end = small_end.next
                    
            elif elem and elem.next:
                elem = elem.next
            else:
                break
        return pivot.next            
            
        
        
