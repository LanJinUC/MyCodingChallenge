def caesarCipherEncryptor(string, key):
	new_string = ""
    for ele in string:
		if ord(ele) + key%26 > 122:
			new_ele = chr(96 + (ord(ele)) + key%26 - 122)
		else:	
			new_ele = chr(ord(ele) + key%26)
		new_string += new_ele
	
	return new_string