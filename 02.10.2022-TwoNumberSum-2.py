array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

# hash table - O(N) Time | O(N) Space
'''
def twoNumberSum(array, targetSum):
	hashTable = {}
	for currentValue in array:
		potentialMatch = targetSum - currentValue
		if potentialMatch in hashTable:
			return [currentValue, potentialMatch]
		else:
			hashTable[currentValue] = True
	return []

print(twoNumberSum(array, targetSum))
'''

# sort - O(NlogN) Time | O(1) Space
'''
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left += 1
		elif currentSum > targetSum:
			right -= 1
	return []

print(twoNumberSum(array, targetSum))
'''

# nested loop - O(N^2) Time | O(1) Space
'''
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		for j in range(i + 1, len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i], array[j]]
	return []

print(twoNumberSum(array, targetSum))
'''