def findClosestValueInBst(tree, target):
	return 	helper(tree, target, tree.value)

def helper(tree, target, closest):
	if tree == None:
		return closest
	
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	
	if tree.value < target:
		return helper(tree.right, target, closest)
	elif tree.value > target:
		return helper(tree.left, target, closest)
	else:
		return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

