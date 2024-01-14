class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_inorder_successor_predecessor(root, key):
    successor = None
    predecessor = None

    while root is not None:
        if root.val < key:
            predecessor = root
            root = root.right
        elif root.val > key:
            successor = root
            root = root.left
        else:
            # Node with the given key is found
            if root.right is not None:
                successor = find_min(root.right)
            if root.left is not None:
                predecessor = find_max(root.left)
            break

    return successor, predecessor

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def find_max(node):
    while node.right is not None:
        node = node.right
    return node

# Example usage:
# Construct a sample BST
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.left = TreeNode(25)
root.right.right
