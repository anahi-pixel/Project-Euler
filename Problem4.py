# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers

def is_Palindrome(num):                                                 #function that checks if the number is a palindrome
	mun = str(num)[::-1]
	return int(mun) == num

def big_Palindrome_under(num):                                          #finds the biggest palindrome
	biggest_Palindrome = 0
	for i in range (int(num/10), num):
		for p in range (int(num/10), num):
			if is_Palindrome(i*p) and i*p > biggest_Palindrome:
				biggest_Palindrome = i*p
	return biggest_Palindrome

print(big_Palindrome_under(1000))