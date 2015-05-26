from euler_12 import divisor_gen

def sum_div(n):
	ds = divisor_gen(n)
	sum = -n
	for d in ds:
		sum += d
	return int(sum)
lookup = [0]
for i in range(1,10001):

	lookup.append(sum_div(i))
total = 0
#print(lookup[220])
for i in range(1,10001):
	l = lookup[i]
	#print(l)
	if l < 10001:
		if lookup[l] == i and i != l: total +=  i
print(total)