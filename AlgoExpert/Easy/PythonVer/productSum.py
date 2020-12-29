# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# Time = O(N) N is the total elements including the sub elements
# Space = O(D) D is the max depth of subarrays
# we need three recursive calls sort of happening at once
# taking up space on the call stack
def productSum(array):
	level = 1
	result = helper(array,level)
	return result

def helper(array,level):
	sub_result = 0
	for ele in array:			
		if type(ele) is list:		
			sub_result += helper(ele,level+1)
		if type(ele) is int:
			sub_result = sub_result + ele		

	return level * sub_result