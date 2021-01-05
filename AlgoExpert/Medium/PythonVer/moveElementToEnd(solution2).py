def moveElementToEnd(array, toMove):
    left_pointer = 0
	right_pointer = len(array) - 1
	
	while left_pointer <= right_pointer:
		if array[right_pointer] == toMove:
			right_pointer -= 1
		
		elif array[left_pointer] == toMove:
			swap(left_pointer, right_pointer, array)
			left_pointer += 1
			right_pointer -= 1
			
		else:
			left_pointer += 1
			
	return array

def swap(i,j,array):
	array[i], array[j] = array[j], array[i]