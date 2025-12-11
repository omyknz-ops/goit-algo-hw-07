def find_min(root):
    if root is None:
        return None
    
    current = root
    while current.left:
        current = current.left
    
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
min_value = find_min(root)
print("Minimum value in the BST is:", min_value)  # Output: Minimum value in the BST is: 5