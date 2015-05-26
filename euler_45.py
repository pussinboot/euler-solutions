#def trian(n):
#	return n*(n+1)//2
#
#def pent(n):
#	return n*(3*n-1)//2
#
#def hexa(n):
#	return n * (2*n - 1)
#
#print(trian(285),pent(165),hexa(143))
#
#i = 286
#j = 1
#k = 1
#t,p,h = trian(i),pent(j),hexa(k)
#while t != p and t != k:
#	t,p,h = trian(i),pent(j),hexa(k)
#	if (p > t and h >= t) or (p >= t and h > t):
#			i += 1
#			j = 0
#			k = 0
#	if p > t:
#		j = 0
#	if h > t:
#		k = 0
#	j += 1
#	k += 1
#print(t)
#

import math
n = 40766
while 1:
    t = n*(n+1)/2
    if (1+math.sqrt(1**2+4*3*2*t))/(2*3) % 1 == 0:
        if (1+math.sqrt(1**2+4*2*t))/(2*2) % 1 == 0:
            print (n*(n+1)//2)
            break
    n += 1