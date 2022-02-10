array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

# My solution
'''
def twoNumberSum(array, targetSum):
	duplicateArray = array
	for numberX in array:
		for numberY in duplicateArray:
			if numberX != numberY and numberX + numberY == targetSum:
				return [numberX, numberY]
	return []

twoNumberSum(array, targetSum)
'''

# Nested (double) loop - O(n^2) time | O(1) space
'''
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		firstNum = array[i]
		for j in range(i + 1, len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum:
				return [firstNum, secondNum]
	return []

print(twoNumberSum(array, targetSum))
'''

# Hash table - O(n) time | O(n) space
'''
def twoNumberSum(array, targetSum):
	nums = {}
	for currentNum in array:
		potentialMatch = targetSum - currentNum
		if potentialMatch in nums:
			return [potentialMatch, currentNum]
		else:
			nums[currentNum] = True
	return []

print(twoNumberSum(array, targetSum))
'''

# Sort - O(nlog(n)) time | O(1) space
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
			left +=1
		elif currentSum > targetSum:
			right -= 1
	return []

print(twoNumberSum(array, targetSum))
'''

