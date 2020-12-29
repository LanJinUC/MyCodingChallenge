# time O(log(N))
# space O(1) in place
# the array needs to be sorted first
def binarySearch(array, target):
	start = 0
	end = len(array) -1
	# // means floor dibision
    mid = 0
	
	while start <= end:
		mid = (start + end)//2 
		if target == array[mid]:
			return mid
		elif target < array[mid]:
			end = mid - 1
		else:
			start = mid + 1
			
	return -1