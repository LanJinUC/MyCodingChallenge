def findThreeLargestNumbers(array):
	sub_arry = array[:3]
	for i in range(3):
		for j in range(2):
			if sub_arry[j] > sub_arry[j+1]:
				sub_arry[j+1], sub_arry[j] = sub_arry[j], sub_arry[j+1]
				
	fstNum = sub_arry[0]
	secNum = sub_arry[1]
	tirdNum = sub_arry[2]
	
	for ele in array:
		if ele >= fstNum:
			tirdNum = secNum
			secNum = fstNum
			fstNum = ele
		elif ele >= secNum:		
			tirdNum = secNum
			secNum = ele
			print(secNum)
		elif ele >= tirdNum:
			tirdNum = ele
		
			
	return [tirdNum,secNum,fstNum]

