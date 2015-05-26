def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

@memodict
def fibb(n):
	if n < 2: return 1
	else: return fibb (n-2) + fibb (n-1)
total = 0
i = 1
new = 0
while new < 4000000:
	new = fibb(i)
	i += 1
	if new % 2 == 0: total += new

#print(total)