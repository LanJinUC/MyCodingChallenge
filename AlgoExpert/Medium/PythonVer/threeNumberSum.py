def threeNumberSum(array, targetSum):
    array.sort()
	result = []
	for ele in array:
		pointer = array.index(ele)
		remainder = targetSum - ele
		dic = {}
		for i in range(pointer + 1, len(array)):
			
			current_ele = array[i]
			current_remainder = remainder - current_ele
			dic[current_remainder] = current_ele
			if current_ele in dic.keys() and current_ele != dic.get(current_ele):				
				result.append([ele, dic.get(current_ele), current_ele]) 
	result.sort()
	return result