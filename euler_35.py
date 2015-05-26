from euler_lib import gen_primes,is_prime
from math import log10

def rotate(n):
	r = [n]
	p = int(log10(n))
	new = n
	for _ in range(p):
		new = 10*(new % 10**p) + (new // 10**p)
		r.append(new)
	return r

#print(rotate(2))
g = gen_primes()
n = 0
count = 0
while n < 1000000:
	n = next(g)
	if 0 not in [is_prime(r) for r in rotate(n)]: count += 1
print(count)
