def isMonotonic(array):
	if not array or len(array) == 1:
		return True
	else:
		first_ele = array[0]
		second_ele = array[1]
		
		if first_ele < second_ele:
			return non_increasing(2,array)			
		elif second_ele < first_ele:
			return non_decreasing(2,array)
		else:
			for i in range(2, len(array)):
				diff = array[i-1] - array[i]
				if diff < 0:
					return non_increasing(i,array)
				elif diff > 0:
					return non_decreasing(i, array)
		return True

def non_increasing(index,array):
	for i in range(index, len(array)):		
		if array[i] < array[i-1]:
			return False
	return True

def non_decreasing(index, array):
	for i in range(index, len(array)):		
		if array[i-1] < array[i]:
			return False
	return True
	
					
					
		
			