class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    """
    Finds the k-th smallest element in a Binary Search Tree (BST).
    
    Args:
    - root: The root of the BST.
    - k: The value of k.
    
    Returns:
    - The k-th smallest element.
    """
    # Helper function to perform in-order traversal and track elements
    def inOrderTraversal(node):
        if not node:
            return []

        # Traverse left subtree
        left = inOrderTraversal(node.left)

        # Process current node
        current_val = node.val

        # Traverse right subtree
        right = inOrderTraversal(node.right)

        # Combine left, current, and right
        return left + [current_val] + right

    # Perform in-order traversal and get the result
    elements = inOrderTraversal(root)

    # Check if k is within the valid range
    if 1 <= k <= len(elements):
        # Return the k-th smallest element
        return elements[k - 1]
    else:
        return None  # k is out of range

# Example usage:
# Constructing a simple BST:      3
#                               /   \
#                              1     4
#                               \
#                                2
root = TreeNode(3)
root.left = TreeNode(1, None, TreeNode(2))
root.right = TreeNode(4)

k = 2
result = kthSmallest(root, k)
print(f"The {k}-th smallest element is: {result}")
