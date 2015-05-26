# finite if multiple of 2 and 5
from euler_3 import *

def len_repeat(n):
	i = 1
	while (10**i -1 )% n != 0:
		i += 1
	return i
#print(1/7)
#print(len_repeat(7))
g = gen_primes()
d = {}
p = next(g)
p = next(g)
p = next(g)
while p < 1000:
	p = next(g)
	#print(1/p)
	d[p] = len_repeat(p)
v=list(d.values())
k=list(d.keys())
print(k[v.index(max(v))])
#print((d))