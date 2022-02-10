array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

# # While loop - O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    arrayIndex = 0
    sequenceIndex = 0
    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrayIndex += 1
    return sequenceIndex == len(sequence)

print(isValidSubsequence(array, sequence))

# For loop - O(n) time | O(1) space
def isValidSubsequence(array, sequence):
	sequenceIndex = 0
	for value in array:
		if sequenceIndex == len(sequence):
			break
		if sequence[sequenceIndex] == value:
			sequenceIndex += 1
	return sequenceIndex = len(sequence)

