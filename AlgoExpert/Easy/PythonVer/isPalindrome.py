def isPalindrome(string):
    lefty = 0
	righty = len(string)-1
	
	while lefty < righty:
		if string[lefty] != string[righty]:
			return False
		lefty += 1
		righty -= 1
	
	return True