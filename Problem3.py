# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

#Defining function to check if a number is prime
def is_Prime(num):
	factors = []
	if num < 2:                                         #1 is not prime
		return False
	for i in range (2, int(math.sqrt(num))+1):          #using a for loop to find all factors between 2 and the sqare root of the number
		if num % i == 0:
			factors.append(i)
	return len(factors) == 0                            # the number is prime if it does not have any factors in that range
		
#Defining a function to find the biggest prime factor		
def big_factor(num):
	factors = []
	for i in range (1, int(math.sqrt(num))+1):
		if num % i == 0 and is_Prime(i):                #adding to the list of prime factors all prime factors before the sqare root of the number
			factors.append(i)
			if is_Prime(int(num/i)):                    #and the ones after the square root
				factors.append(num/i)
	return factors[-1]		                            #returning the last prime factor of the list

print(big_factor(600851475143))