# the function will add all numbers from 
# zero to the maximum specified number

def magic_sum(maximum):
	total = 0; # initialize the variable total to zero
	for x in range(maximum + 1):
		total = total + x
	return total