# stupid way
#def problem5(n):
#	t = 2
#	test = list(range(2,n+1))
#	while len(test) != 0:
#		p = test.pop()
#		if t % p != 0:
#			t += 2520
#			test = list(range(2,n+1))
#	return t
#
#print(problem5(20))

from euler_3 import *
factors = []
for i in range(2,21):
	ps = prime_factors(i)
	for p in ps:
		if p not in factors:
			factors.append(p)
		elif ps.count(p) > factors.count(p):
			factors.append(p)
ans = 1
for n in factors:
	ans *= n
print(ans)
