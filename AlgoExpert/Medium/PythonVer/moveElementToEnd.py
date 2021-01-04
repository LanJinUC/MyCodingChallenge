def moveElementToEnd(array, toMove):
	for ele in array:
		if ele == toMove:
			del array[array.index(ele)]
			array.append(ele)			
		
	return array