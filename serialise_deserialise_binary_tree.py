# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Codec:

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        stack = []
        depth = self.depth(root)
        if depth == 0:
            return []
        if depth == 1:
            return [root.val]
        nodes = sum([ pow(2, i) for i in range(depth)])
        #print(depth, nodes)
        stack.append(root)
        while len(stack) > 0:
            topelem = stack.pop(0)
            if topelem == None:
                output.append("null")
                continue 
            if topelem.left:
                stack.append(topelem.left)
            else:
                stack.append(None)
            if topelem.right:
                stack.append(topelem.right)
            else:
                stack.append(None)
            output.append(topelem.val)
            #print(len(output), output, nodes)
            if len(output) >= nodes:
                stack.clear()
        #print(output)
        return output
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        levels = math.log(len(data) + 1)/math.log(2)
        #print("Total levels", levels)
        root = TreeNode(data[0])
        stack = [root]
        curr_elem = 1
        if levels == 1:
            return root
        while len(stack) > 0:
            topelem = stack.pop(0)
            topelem.left = TreeNode(data[curr_elem])
            curr_elem += 1
            topelem.right = TreeNode(data[curr_elem])
            curr_elem += 1
            stack.append(topelem.left)
            stack.append(topelem.right)
            if curr_elem >= len(data):
                break
        return root
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
