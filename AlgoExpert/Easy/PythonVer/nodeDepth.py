def nodeDepths(root):
	total_depth = 0
	helper(root, 0, total_depth)
	return total_depth

def helper(node, depth, total_depth):	
	#edge case:
	#if there is one child is None
	if node == None:
		return 
	
	print("node is:" + str(node.value) + " depth is: " + str(depth))
	#if we are at the leaf node
	
	
	if node.left is None and node.right is None:
		total_depth += depth
		
		return 
	
	
	
	helper(node.left, depth + 1, total_depth)
	helper(node.right, depth + 1, total_depth)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None