def find_max(root):
    if root is None:
        return None
    
    current = root
    while current.right:
        current = current.right
    
    return current.key

# Example usage:
# Assuming a binary search tree node structure like this:
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# Constructing a simple BST for demonstration
#        10
#       /  \
#      5   15

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
max_value = find_max(root)
print("Maximum value in the BST is:", max_value)  # Output: Maximum value in