def runLengthEncoding(string):
    output = ""
	counter = 1
	for i in range(len(string)-1):
		
		if string[i] == string[i+1]:
			counter += 1
			print(counter)
		else:
			if counter > 9:
				mul = (counter - counter % 9) // 9
				output += mul * ("9" + string[i])
				output += str(counter % 9)
	
			else:
				output += str(counter)
		
			output += string[i]
			counter = 1
			
	
	if counter > 9:
			mul = (counter - counter % 9) // 9
			output += mul * ("9" + string[-1])
			output += str(counter % 9)

	else:
		output += str(counter)

	output += string[-1]
		
	return output