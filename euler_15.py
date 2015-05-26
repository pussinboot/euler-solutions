def nck(n,k): # n choose k
	return fact(n)/(fact(k)*fact(n-k))

def fact(n): 
	if n <= 1: return 1
	else: return n*fact(n-1)

#print(nck(2,2))
#print(fact(10))

path = 1
for i in range(20):
	path *=2*20-i
	path /= (i + 1)

print(path)
