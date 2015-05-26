from euler_lib import prime_factors
#print(prime_factors(20))

def reduce_primes(pf):
	return ([x**pf.count(x) for x in pf])
	# not what we need

def n_dist(pf):
	return len(set(pf))

def check_n(last,n):
	return 0 not in [n_dist(a)==n for a in last]

i = 647
last_four = [prime_factors(i-3),prime_factors(i-2),prime_factors(i-1),prime_factors(i)]
#print(last_four)
#last_four.pop(0)
#print(last_four)
#last_four.append(prime_factors(i+1))
#print(last_four)
#print(check_n(last_four[:3],3))
while not check_n(last_four,4):
	i += 1
	last_four.pop(0)
	last_four.append(prime_factors(i))
print(i)

# this is reverse of what should be done
# should multiply together factors and count them, .-.