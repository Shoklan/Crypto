# Collin Mitchell
# Vogel.py | Application to create the Vogel Quintuple Disk Cipher from paper 
#          | "THE INDEX OF COINCIDENCE AND ITS APPLICATIONS IN CRYPTANALYSIS."
# 2015 February 8th

# Variables  | These are the static rings for the Vogel Disk
plainList  = ['plain', 9, 17, 4, 14, 10, 7, 21, 11, 16, 6, 20, 19, 12, 3, 5, 15, 2, 1, 13, 18, 8, '', '', '', '']
innerList1 = ['p', 'k', 'v', 'a', 'u', 'f', 'q', 'z', 'e', 'r', 'h', 'y', 'g', 'w', 'j', 'o', 'i', 'd', 'm', 'n', 'c', 't', 'x', 's', 'b', 'l']
innerList2 = ['r', 'b', 'n', 'h', 'c', 'q', 'a', 'o', 'x', 'g', 'f', 'z', 'm', 'y', 'l', 'p', 'u', 'k', 'e', 't', 'd', 'j', 'v', 's', 'w', 'i']
innerList3 = ['e', 'd', 's', 'z', 'x', 'c', 'm', 'l', 'r', 'y', 'a', 'w', 'j', 'b', 'q', 'i', 'h', 'v', 'k', 'p', 'u', 'f', 'o', 'g', 't', 'n']
innerList4 = ['p', 'y', 'a', 'c', 'v', 'x', 'z', 'w', 'm', 't', 'f', 'n', 'u', 'i', 'o', 's', 'e', 'h', 'j', 'r', 'd', 'l', 'g', 'k', 'q', 'b']
innerList5 = ['a', 'e', 't', 'j', 'u', 'd', 'm', 'v', 'z', 'n', 'w', 'h', 'x', 'o', 'g', 'y', 'k', 'f', 'r', 'l', 'q', 'b', 'p', 'c', 'i', 's']

cipher = ''
index = 18   # 

#   ............ from the user input
def removeSpaces(inputString):
	while(' ' in inputString):
		blankIndex = inputString.index(' ')
		inputString = inputString[:blankIndex] + inputString[blankIndex+1:]
	return inputString

def insertSpaces(cipher):
	temp = ''
	
	while len(cipher) > 5:
		temp = temp + cipher[:5] + ' '
		cipher = cipher[5:]

	return temp


# self
def convertLowerCase(inputString):
	return inputString.lower()

#   ...............  from the user input
def createParamList(inputString):
	tempList = []
	
	while len(inputString) > 5:
		tempList.append(inputString[:5])
		inputString = inputString[5:]
	return tempList

# spin in the cipher disk
def createCipher(param, index):
	temp = ''
	if index in [0, 25, 24, 23, 22]: index = 1 # ignore blank labels
	
	# generate the cipher based on the length of the parameter input
	if len(param) == 5:
		index1 = innerList1.index(param[0])
		index2 = innerList2.index(param[1])
		index3 = innerList3.index(param[2])
		index4 = innerList4.index(param[3])
		index5 = innerList5.index(param[4])

		temp = temp + (innerList1[ (index1 + index) % 26])
		temp = temp + (innerList2[ (index2 + index) % 26])
		temp = temp + (innerList3[ (index3 + index) % 26])
		temp = temp + (innerList4[ (index4 + index) % 26])
		temp = temp + (innerList5[ (index5 + index) % 26])
	elif len(param) == 4:
		index1 = innerList1.index(param[0])
		index2 = innerList2.index(param[1])
		index3 = innerList3.index(param[2])
		index4 = innerList4.index(param[3])

		temp = temp + (innerList1[ (index1 + index) % 26])
		temp = temp + (innerList2[ (index2 + index) % 26])
		temp = temp + (innerList3[ (index3 + index) % 26])
		temp = temp + (innerList4[ (index4 + index) % 26])
	elif len(param) == 3:
		index1 = innerList1.index(param[0])
		index2 = innerList2.index(param[1])
		index3 = innerList3.index(param[2])

		temp = temp + (innerList1[ (index1 + index) % 26])
		temp = temp + (innerList2[ (index2 + index) % 26])
		temp = temp + (innerList3[ (index3 + index) % 26])
	elif len(param) == 2:
		index1 = innerList1.index(param[0])
		index2 = innerList2.index(param[1])

		temp = temp + (innerList1[ (index1 + index) % 26])
		temp = temp + (innerList2[ (index2 + index) % 26])
	elif len(param) == 1:
		index1 = innerList1.index(param[0])

		temp = temp + (innerList1[ (index1 + index) % 26])

	#return values
	return temp, index + 1

if 	__name__ == '__main__':
	# inital set up
	from sys import argv
	inputString = argv[1]
	print inputString

	# prepare data for mutilation!
	inputString = convertLowerCase(inputString)
	inputString = removeSpaces(inputString)
	parameterList = createParamList(inputString)
	
	# DATALIZE THE DATA!
	for item in parameterList:
		temp, index = createCipher(item, index)
		cipher = cipher + temp
	
	# format output with spaces
	cipher = insertSpaces(cipher)

	# print output as to compare
	print cipher

	raw_input()
