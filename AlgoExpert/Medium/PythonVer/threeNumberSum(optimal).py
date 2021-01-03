def threeNumberSum(array, targetSum):
	result = []
	array.sort()
    for ele in array:
		current_index = array.index(ele)
		left_pointer = current_index + 1
		right_pointer = len(array) - 1
		current_remainder = targetSum - ele
		while left_pointer < right_pointer:
			current_sum = array[left_pointer] + array[right_pointer]
			if current_sum == current_remainder:
				result.append([ele, array[left_pointer], array[right_pointer]])
				left_pointer += 1
				right_pointer -= 1
			elif current_sum < current_remainder:
				left_pointer += 1
			else:
				right_pointer -= 1
				
	return result