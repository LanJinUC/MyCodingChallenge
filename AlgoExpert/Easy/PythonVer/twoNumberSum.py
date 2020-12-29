def twoNumberSum(array, targetSum):
    dic = {}
	for ele in array:
		remainder = targetSum - ele
		dic[remainder] = ele
		if ele in dic.keys() and ele != dic.get(ele):
			return [ele, dic.get(ele)]
	
	return []