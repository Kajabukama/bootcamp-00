'''
	A prime number is one that is only divisible by 1 and itself. 
	Therefore, if we want to generate a list of non-primes under 50 we can do so by generating multiples.
'''

def generate_multiples(number):
	list_non_primes = set(j for i in range(2, 8) for j in range(i*2, number, i))
	return non_primes

def generate_prime(number):
	if number == 0:
		return 'Invalid argument,input must be greater than zero'
	elif number < 0 :
		return 'Invalid argument,no negative input allowed'
	elif type(number) == str:
		return 'Invalid argument,no string input allowed'
	elif type(number) == float:
		return 'Invalid argument,no float input allowed'
	else:
		non_primes = generate_multiples(number)
		list_prime_numbers = [x for x in range(2, number) if x not in non_primes]
		return prime_numbers


