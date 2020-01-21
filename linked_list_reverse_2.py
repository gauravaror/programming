# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        head_copy = head
        current_index = 1
        start_reverse = None
        end_reverse = None
        prev = None
        start_reverse_next = None
        while current_index < m:
            if current_index == m-1:
                start_reverse = head
            if head.next:
                current_index += 1
                head = head.next
        while True:
            if current_index > n:
                break
            else:
                temp_next = head.next
                head.next = prev
                if current_index == m:
                    start_reverse_next = head
                prev = head
                if current_index == n:
                    end_reverse = head
                    end_reverse_next = temp_next
                head = temp_next
                current_index += 1
        if start_reverse:
            start_reverse.next = end_reverse
            start_reverse_next.next = head
            return head_copy
        elif end_reverse:
            start_reverse_next.next = end_reverse_next
            return end_reverse
        else:
            return head
        return head_copy
