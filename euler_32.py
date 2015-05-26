nums = '123456789'
def pandigital(a,b,n): # check that a, b and a*b only have 1 through n
	set = nums[:n+1]
	check = str(a)+str(b)+str(a*b)
	if len(check) != n: return 0
	if containsAll(check,set): return a*b
	else: return 0

def containsAll(str, set):
    """Check whether 'str' contains ALL of the chars in 'set'"""
    return 0 not in [c in str for c in set]

#print(pandigital(39,186,9))
res = set()
for a in range(1,100):
	for b in range(100,10000):
		res.add(pandigital(a,b,9))
tor = 0
for a in res:
	tor += a

print(tor)