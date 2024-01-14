class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Node with one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children
        successor = find_min(root.right)
        root.key = successor.key
        root.right = delete_node(root.right, successor.key)

    return root

# Example usage:
# Create a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Delete a node (e.g., node with key 5)
root = delete_node(root, 5)
