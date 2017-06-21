import sys
for line in sys.stdin:
	letter = line
vowel = ['a','e','i','o','u','A','E','I','O','U']
if letter in vowel:
	print("Vowel")
else:
	print("Consonent")
