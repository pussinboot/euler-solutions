from functools import reduce

def prod(iterable):
	return reduce(operator.mul, iterable, 1)


n1 = 1
n2 = 1
#print(9+2*(90))
n = [9, 90, 900, 9000, 90000,900000,9000000]
d = [1, 2, 3, 4, 5, 6, 7]
ns = []
nn = []
for i in range(len(n)):
	ns.append(sum([a*b for a,b in zip(n[:i+1],d[:i+1])]))
	nn.append(sum(n[:i+1]))

def check(num):
	i = 0
	while num > ns[i]:
		i += 1
	if i == 0: 
		return num
	num -= ns[i-1]
	dig = num % (i + 1)
	#print('dig',dig)
	rem = num // (i + 1) + nn[i-1] 
	#print('rem',rem)
	return rem // 10**i
	#print(num)


#check(187)
#test = range(1,100)
#ss = ' '
#for t in test:
#	ss += str(t)
#print(ss)
#print(len(ss)-1)
#print(ss[187])#

for i in range(2,7):
	print(10**i,':',check(10**i))