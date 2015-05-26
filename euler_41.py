from euler_lib import *

nums = '123456789'

def containsAll(str, set):
    """Check whether 'str' contains ALL of the chars in 'set'"""
    return 0 not in [c in str for c in set]

p = gen_primes()
n = 1
#while n < 7642513:
#	n = next(p)
pp = str(n)
#ppl = 7642513
while len(pp) < 9:
	n = next(p)
	pp = str(n)
	#print(pp,len(pp),nums[:len(pp)])
	if containsAll(pp,nums[:len(pp)]):
		if n > ppl: 
			ppl = n
			print(ppl)


print(ppl)

