# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        prev = None
        if not head:
            return head
        while (temp.next):
            next_temp = temp.next
            if temp.val == next_temp.val:
                while(next_temp.val == temp.val):
                    next_temp = next_temp.next
                    if not next_temp:
                        break
                if prev == None:
                    head = next_temp
                else:
                    prev.next = next_temp
                    
                if not next_temp:
                    break
                    
                temp = next_temp
                
            else:
                prev = temp
                temp = next_temp
        return head         
