#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

mult3 = 0          #multiples of 3
mult5 = 0          #multiples of 5 
mult3and5 = 0      #multiples of both

for i in range (1,1000,1):
	if i % 3 == 0 and i % 5 != 0:
		mult3 = mult3 + i                     #updating the variables
	if i % 3 != 0 and i % 5 == 0:	
		mult5 = mult5 + i
	if i % 3 == 0 and i % 5 == 0:
		mult3and5 = mult3and5 + i

sum = mult3and5 + mult5 + mult3

print(sum) 
