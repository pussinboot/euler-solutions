#def trip(m,n):
#	# m < n
#	return n**2 - m**2, 2*m*n, n**2 + m**2
#def sumtrip(m,n): # m < n
#	return 2*n**2 + 2*m*n
##print(trip(1,2))
##print(sumtrip(1,2))
#
#ans = [0]*1000
#m = 1
#n = 2
#s = 0
#while m < 1000:
#	s = sumtrip(m,n)
#	if s >= 1000: 
#		m += 1
#		n = m + 1
#	else:
#		ans[s] = ans[s] + 1
#		n += 1
#
#print(ans.index(max(ans)))
from math import sqrt,floor

def gcd(x,y):

	if x < y:
		t = x
		x = y
		y = t

	while (x % y != 0):
		temp = x
		x = y
		y = temp % x
		
	return y

pMax = 0
tMax = 0
m = 0
k = 0
 
for s in range(1001):
	t = 0
	mlimit = floor(sqrt(s / 2));
	for m in range(2,mlimit + 1):
		if ((s / 2) % m == 0):
			if (m % 2 == 0):
				k = m + 1
			else:
				k = m + 2
			while (k < 2 * m and k <= s / (2 * m)):
				 if (s / (2 * m) % k == 0 and gcd(k, m) == 1):
				     t+= 1
				 k += 2

	if (t > tMax):
		tMax = t
		pMax = s
			
print(pMax)