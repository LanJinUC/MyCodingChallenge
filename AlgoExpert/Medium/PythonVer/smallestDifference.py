def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	first_pointer = 0
	second_pointer = 0
	result_pair = [arrayOne[first_pointer], arrayTwo[second_pointer]]
	result_abs = abs(arrayOne[first_pointer] - arrayTwo[second_pointer])
	
	while first_pointer < len(arrayOne) and second_pointer < len(arrayTwo):
		fst_num = arrayOne[first_pointer]
		sec_num = arrayTwo[second_pointer]
		current_abs = abs(fst_num - sec_num)
		current_pair = [fst_num, sec_num]
	
		if current_abs == 0:
			return current_pair
		
		else:		
			if current_abs < result_abs:
				result_pair = current_pair
				result_abs = current_abs
			if fst_num < sec_num:
				first_pointer += 1
			else:
				second_pointer += 1
	return result_pair		