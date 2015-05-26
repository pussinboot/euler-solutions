from euler_2 import memodict

@memodict
def seq(n):

	tor = 1
	while n % 2 == 0:
		tor += 1
		n = n/2
	if n == 1:
		return tor
	return tor + seq(3 * n + 1)
max_n = 0
maxx = 0

for i in range(500000,1000000):
	t = seq(i)
	if t > maxx: 
		maxx = t
		max_n = i

print(max_n)

#print(seq(13))
