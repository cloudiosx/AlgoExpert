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