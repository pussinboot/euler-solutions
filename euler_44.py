pents = set()


def pent(n):
	return n*(3*n-1)//2

def sum_diff_check(n,a) :
	if (n > a) and (n - a in pents) and (n + a in pents):
		return True
	return False

for i in range(1,11):
	print(pent(i))

for i in range(1,10000):
	pents.add(pent(i))

pj = 0
pk = 0
d = 10000000000

for p in pents:
	for p2 in pents:
		if(sum_diff_check(p,p2)):
			if p-p2 < d:
				print(p,p2,p-p2)
				d = p-p2