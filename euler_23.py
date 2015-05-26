lookup = []
a = []
from math import sqrt, ceil

def sum_div( n ) :
	root = int( ceil( sqrt( n ) ) )
	total = 1
	for i in range( 2, root ) :
		if n % i == 0 :
			total += i + n // i
	if n != 1 and n == root * root:
		total += root
	return total

def check_sum(n):
	i = 0
	j = 0
	while a[i] < n:		
		while a[i] + a[j] <= n:
			if a[i] + a[j] == n: return 0
			j += 1
		i += 1
	return n

def isSumOfTwoAbundants( n ) :
	return any( (n-a in abundants) for a in abundants )

abundants = set()
total = 0

for n in range( 1, 28124 ) :
	if sum_div( n ) > n :
		abundants.add( n )
	if not isSumOfTwoAbundants( n ) :
		total += n
		
print( total)
#
#
#for i in range(1,28124):`
#	tmp = sum_div(i)
#	lookup.append(tmp)
#	if tmp > i: a.append(tmp)
#
##s = []
##for i in range(len(a)):
##	for j in range(len(a)):
##		s.append(a[i]+a[j])
##
##total = 0
#for i in range(1,28124):
#	if i not in s: total+= i
#print(total)#