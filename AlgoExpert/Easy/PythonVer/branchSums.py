class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sumList = []
    helper(root, 0, sumList)
	return sumList

def helper(node, total, sumList):	
	#edge case:
	#if there is one child is None
	if node == None:
		return 
	
	newTotal = total + node.value
	print(newTotal)
	#if we are at the leaf node
	if node.left is None and node.right is None:
		sumList.append(newTotal)
		return
	
	helper(node.left, newTotal, sumList)
	helper(node.right, newTotal, sumList)