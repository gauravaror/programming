# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, 0))
        level = 0
        ls = [[]]
        all_null = True
        #print(root)
        def get_level_len(lis):
            start = 0
            end = len(lis) -1
            while start <= end:
                #print(start, end, lis)
                if lis[start] != None and lis[end] != None:
                    return end - start + 1
                if lis[start] == None:
                    start += 1
                if lis[end] == None:
                    end -= 1
                if start == end:
                    if lis[start]:
                        return 1
                    else:
                        return 0
                    
            return 0
        
        #return
        notnull_level = 0
        while len(stack) > 0:
            celem, cur_level = stack.pop(0)
            if len(stack) > 0:
                next_level = stack[0][1]
            else:
                next_level = cur_level
            #print(celem)
            if celem and celem.left:
                stack.append((celem.left, cur_level + 1))
                all_null = False
                notnull_level = notnull_level if notnull_level > cur_level + 1 else cur_level + 1
            elif notnull_level == cur_level + 1:
                stack.append((None, cur_level + 1))  
            
            if celem and celem.right:
                stack.append((celem.right, cur_level + 1))
                all_null = False
                notnull_level = notnull_level if notnull_level > cur_level + 1 else cur_level + 1
            elif next_level == cur_level:
                stack.append((None, cur_level + 1))

            if level != cur_level:
                if all_null:
                    break
                if celem:
                    all_null = False
                else:
                    all_null = True
                level = cur_level
                #ls.append([])
            #if celem:
            #    ls[-1].append(celem.val)
            #else:
            #    ls[-1].append(celem)
        #print(ls)
        #mina = [get_level_len(i) for i in ls]
        #print(mina)
        return
        return max(mina)
