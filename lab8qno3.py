class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def find_min(node):
    # Traverse to the leftmost node
    while node.left is not None:
        node = node.left
    return node.val

def find_max(node):
    # Traverse to the rightmost node
    while node.right is not None:
        node = node.right
    return node.val

# Example usage:
# Construct a simple BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Find minimum and maximum values
min_val = find_min(root)
max_val = find_max(root)

print("Minimum valu
