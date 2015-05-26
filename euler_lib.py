from math import ceil,sqrt
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

def gen_fibb():
    """ Generate an infinite sequence of fibonacci numbers.
    """
    f1 = 0
    f2 = 0
    new = 1

    while True:
        yield new
        f1 = f2
        f2 = new
        new = f1 + f2

def sum_div( n ) :
	root = int( ceil( sqrt( n ) ) )
	total = 1
	for i in range( 2, root ) :
		if n % i == 0 :
			total += i + n // i
	if n != 1 and n == root * root:
		total += root
	return total

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def prime_factors(n):
    t = n
    p = gen_primes()
    toReturn = []
    f = next(p)
    while t != 1:
        if t % f == 0:
            toReturn.append(f)
            t = t/f
        else:
            f = next(p)
    return toReturn

@memodict
def is_prime(n):
	if n < 2: return False
	elif n == 2: return True
	for i in range(2,ceil(sqrt(n))+1):
		if n % i == 0: return False
	return True

@memodict
def fact(n):
	if n < 2: return 1
	else: return n*fact(n-1)

def py_trips(a,b,c,d):
    """ resursive pythagorean triplets.
    """
    if d > 0:
    	return [py_trips(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c,d-1),py_trips(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c,d-1),py_trips(2*b - a + 2*c, b - 2*a + 2*c, 2*b - 2*a + 3*c,d-1)]
    else:
    	return (a,b,c)


if __name__ == '__main__':
	print("testing")
	#print(py_trips(3,4,5,10))