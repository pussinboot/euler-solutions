from math import ceil, sqrt

def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__
@memodict
def is_prime(n):
	if n < 2: return False
	for i in range(2,ceil(sqrt(n))+1):
		if n % i == 0: return False
	return True

def count_primes(a,b):
	n = 0
	going = True
	while going:
		if is_prime(n**2 + a * n + b): n += 1
		else: going = False
	return n

maxn = 0
maxab = 0

for a in range(-1000,1001):
	for b in range(-1000,1001): # can reduce to just the primes up to 1000
		n = count_primes(a,b)
		if n > maxn:
			maxn = n
			maxab = a*b

print(maxab)