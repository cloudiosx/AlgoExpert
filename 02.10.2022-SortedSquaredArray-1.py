array = [1, 2, 3, 5, 6, 8, 9]
'''
def sortedSquaredArray(array):
	newArray = []
	valueIndex = 0
	for value in array:
		newArray.append(array[valueIndex]**2)
		valueIndex += 1
	newArray.sort()
	return newArray

print(sortedSquaredArray(array))
'''

'''
def sortedSquaredArray(array):
	valueIndex = 0
	for value in array:
		array[valueIndex] = array[valueIndex]**2
		valueIndex += 1
	return sorted(array)

print(sortedSquaredArray(array))
'''

# AlgoExpert Brute Force - O(nLogn) Time | O(n) Space
'''
def sortedSquaredArray(array):
	newArray = [0 for _ in array]
	for index in range(len(array)):
		value = array[index]
		newArray[index] = value ** 2
	newArray.sort()
	return newArray
'''

# AlgoExpert Brute Force - O(nLogn) Time | O(n) Space
def sortedSquaredArray(array):
	newArray = [0 for _ in array]
	leftPointerIndex = 0
	rightPointerIndex = len(array) - 1

	for index in reversed(range(len(array))):
		if abs(array[leftPointerIndex]) > abs(array[rightPointerIndex]):
			newArray[index] = array[leftPointerIndex] ** 2
			leftPointerIndex += 1
		else:
			newArray[index] = array[rightPointerIndex] ** 2
			rightPointerIndex -= 1
	return newArray



# def sortedSquaredArray(array):
# 	newArray = []
# 	left = 0
# 	right = len(array) - 1
# 	while left < right:
# 		if abs(array[right]) > abs(array[left]):
# 			newArray = [array[right]**2] + newArray
# 			right -= 1
# 		elif abs(array[left]) > abs(array[right]):
# 			newArray = [array[left]**2] + newArray
# 			left += 1
# 	newArray = [array[left]**2] + newArray
# 	return newArray

print(sortedSquaredArray(array))