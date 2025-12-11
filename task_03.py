def find_sum(root):
    if root is None:
        return 0
    
    left_sum = find_sum(root.left)
    right_sum = find_sum(root.right)
    
    return root.key + left_sum + right_sum
