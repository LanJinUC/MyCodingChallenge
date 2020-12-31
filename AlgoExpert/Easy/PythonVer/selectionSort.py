def selectionSort(array):
	
	for i in range(0, len(array)):
		largest = array[i]
		largest_index = i
		for k in range(i+1, len(array)):
			if array[k] >= largest:
				largest = array[k]
				largest_index = k
		
		while largest_index != 0:
			swap(largest_index, largest_index-1, array)
			largest_index -= 1

	return array



def swap(i, j, array):
	array[i], array[j] = array[j], array[i]