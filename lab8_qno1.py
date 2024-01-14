class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_bst(root, value):
    # Base Cases: root is null or value is present at root
    if root is None or root.key == value:
        return root

    # If the value is smaller than the root's key, then search in the left subtree
    if value < root.key:
        return search_bst(root.left, value)

    # If the value is larger than the root's key, then search in the right subtree
    return search_bst(root.right, value)
