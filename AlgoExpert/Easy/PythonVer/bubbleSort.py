# average Time O(n^2)
# Space O(1)
def bubbleSort(array):
	while True:
		counter = 0	
		for j in range(len(array)-1):
			if array[j] > array[j+1]:
				counter += 1
				array[j+1], array[j] = array[j], array[j+1]
		if counter == 0:
			break
	
	return array