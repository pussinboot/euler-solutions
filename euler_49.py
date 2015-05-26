from euler_lib import gen_primes

def all_perms(str):
	if len(str) <=1:
		yield str
	else:
		for perm in all_perms(str[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + str[0:1] + perm[i:]

gp = gen_primes()
last = 0
testset = []
while last < 10000:
	last = next(gp)
	if last > 1000: testset.append(last)

#print(len(testset))

#def check1(n,rest):
#
#	return [x for x in rest if (2*x - n in rest )]
#
#def check2(n,rest):
#
#	return [int(x) for x in all_perms(str(n)) if (int(x) in rest)]
#
#set1 = set(check1(1487,testset))
#set2 = set(check2(1487,testset))
#print(set1 & set2)
#for f in testset:
#	t1 = check1(f,testset)
#	t2 = []
#	for p in all_perms(str(f)):
#		if int(p) in t1: 
#			t2.append(int(p))
#	if len(t2) > 2: 
#		if abs(t2[0] - t2[1] == f):
#			print(t2[0])

pd = {}
for pi in testset:
	spi = sorted(str(pi))
	pd.setdefault(spi, []).append(pi)

for i, pi in enumerate(testset):
	if pi < 1000 or pi == 1487: continue
	spi = sorted(str(pi))
	pals = pd[spi] 
	if len(pals) < 3: continue
	for pj in pals:
		if pj <= pi: continue 
		if sorted(str(pj)) != spi: continue
		diff = pj - pi
		pk = pj+diff
		if pk in pals:
			print ("%s%s%s" % (pi, pj, pk))