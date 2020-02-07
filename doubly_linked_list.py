"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        tmp = head
        saved = None
        print(head)
        while True:
            if head == None:
                break
            if not (head.child == None):
                child = self.flatten(head.child)
                head.child  = None
                next_yes = head.next
                head.next = child
                child.prev = head
                while child.next:
                    child = child.next
                child.next = next_yes
                if next_yes:
                    next_yes.prev = child
                head = next_yes
            else:
                head = head.next
        return tmp
