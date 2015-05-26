from euler_lib import gen_primes,is_prime
from math import log10

def trunc_lr(n):
	r = [n]
	p = int(log10(n))
	for i in range(1,p+1):	
		r.append(n % 10**i)
		r.append(n // 10**i)
	return r
#print(trunc_lr(3797))
g = gen_primes()
n = next(g)
n = next(g)
n = next(g)
n = next(g)
count = 0
total = 0
while count < 11:
	n = next(g)
	if 0 not in [is_prime(r) for r in trunc_lr(n)]:
		count += 1
		total += n
		
print(total)