from euler_3 import *
def sum_below(n):
	p = gen_primes()
	x = 0
	sum = 0
	while x < n:
		sum += x
		x = next(p)
	return sum

print(sum_below(2000000))
