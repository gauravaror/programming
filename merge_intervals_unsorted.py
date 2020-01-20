from typing import List
class TreeNode:
    def __init__(self, start, end, head):
        self.start = start
        self.end = end
        self.right = None
        self.left = None
        self.head = head
        self.middle = (start + end)//2
        
        
class Solution:
    def __ini__(self):
        self.answer = []

    def add(self, root, node):
        if (node[1] < root.middle):
            if not root.left:
                root.left = TreeNode(node[0], node[1], root)
            else:
                self.add(root.left, node)
        else:
            if not root.right:
                root.right = TreeNode(node[0], node[1], root)
            else:
                self.add(root.right, node)
    def tprint(self, root):
        if root.left:
            self.tprint(root.left)
        print([root.start, root.end])
        if root.right:
            self.tprint(root.right)

    def query(self, root):
        print("Running ", root.start, root.end, self.answer)
        lef = None
        rig = None
        if root.left:
            lef = self.query(root.left)
        if root.right:
            rig = self.query(root.right)

        current = None
        if lef:
            if lef[1] < root.start:
                self.answer.append(lef)
            else:
                current =  [lef[0], root.end]
        if rig:
            if current and current[1] >  rig[0]:
                current = [current[0], rig[1]]
            else:
                if current:
                    self.answer.append(current)
                else:
                    if root.end < rig[1]:
                        self.answer.append([root.start, root.end])
                    else:
                        rig = [root.start, rig[1]]
                current = rig
        if not lef or rig:
            current = [root.start, root.end]
        print("Leaving", root.start, root.end, current, self.answer)
        return current

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.answer = []
        if len(intervals) == 0:
            return None
        elif len(intervals) == 1:
            root = TreeNode(intervals[0][0], intervals[0][1], None)
            return root
        else:
            root = TreeNode(intervals[0][0], intervals[0][1], None)
        for i in intervals[1:]:
            self.add(root, i)
        self.tprint(root)
        current = self.query(root)
        self.answer.append(current)
        return self.answer

        
        
sol = Solution()
print('Answer', sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print('Answer', sol.merge([[8,10], [1,3],[2,6],[9,11],[15,18]]))

