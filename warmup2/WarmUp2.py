# @Brandon Thacker
# www.codingbat.com PYTHON WarmUp1 Problems and Solutions 

'''STRING_TIMES
Given a string and a non-negative int n, return a larger string that is n copies of the original string. 

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''

def string_times(str, n):
	return str * n

'''FRONT_TIMES
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front; 

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(str, n):
	strLen = len(str)
	if (strLen < 3):
		sub = str[0:strLen]
	else:
		sub = str[0:3]
	return sub * n

'''STRING_BITS
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_bits(str):
	strLen = len(str)
	newString = ""
	for x in range(0, strLen, 2):
		newString += str[x]
		x += 1
		

	return newString

'''STRING_SPLOSION
Given a non-empty string like "Code" return a string like "CCoCodCode". 

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
	strLen = len(str)
	newString = ""
	j = 1
	for x in range(0, strLen):
		newString += str[0:j]
		j += 1
	return newString

'''LAST2
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def last2(str):
	strLen = len(str)
	sub = str[strLen - 2:strLen]
	counter = 0
	for x in range(0, strLen - 2):
			if (str[x:x+2] == sub):
				counter += 1

	return counter

'''ARRAY_COUNT9

Given an array of ints, return the number of 9's in the array. 

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''

def array_count9(nums):
	counter = 0
	arLen = len(nums)
	for x in range(0, arLen):
		if (nums[x] == 9):
			counter += 1

	return counter

'''ARRAY_FRONT9
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4. 

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

def array_front9(nums):
	if (len(nums) > 4):
		arLen = 4
	else:
		arLen = len(nums)
	for x in range(0, arLen):
		if (nums[x] == 9):
			return True
	return False

'''ARRAY123
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

def array123(nums):
	for x in range(0, len(nums) - 2):
		if (nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3):
			return True
	return False

'''STRING_MATCH
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. 

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):
	counter = 0
	aLen = len(a)
	bLen = len(b)
	small = min(aLen, bLen)
	for x in range(0, small - 1):
		if (a[x] == b[x] and a[x+1] == b[x+1]):
			counter += 1
	return counter

