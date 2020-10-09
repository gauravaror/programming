# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f"{root.val},{len(left)},{len(right)},{left}{right}"
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        def get_val(index):
            while index < len(data):
                if data[index] == ',':
                    return index
                index += 1
            raise "not expected to run out of commas"
        pind = 0
        ind = get_val(pind)
        root = TreeNode(int(data[pind:ind]))
        pind = ind + 1
        ind = get_val(pind)
        left_len = int(data[pind:ind])
        pind = ind + 1
        ind = get_val(pind)
        right_len = int(data[pind:ind])
        root.left = self.deserialize(data[ind+1:ind+1+left_len])
        root.right = self.deserialize(data[ind+1+left_len:])
        return root
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
