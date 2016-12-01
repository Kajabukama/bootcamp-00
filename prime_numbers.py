# a function that generate prime numebers from 0 to n
import math
def generate_prime(number):
	# empty list to hold the generate prime numbers
	list_prime = []
	
	if number == 0:
		return 'Invalid argument,input must be greater than zero'
	elif number < 0 :
		return 'Invalid argument,no negative input allowed'
	elif type(number) == str:
		return 'Invalid argument,no string input allowed'
	elif type(number) == float:
		return 'Invalid argument,no float input allowed'
	else:
		for i in range(2,number):
			if (i % 2 != 0):
				list_prime.append(i) 	
		return list_prime

# print(generate_prime(0))
