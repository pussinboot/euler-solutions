pp = [0,1,2,3,4,5,6,7,8,9]
def fact(n):
	if n <= 1: return 1
	else: return n * fact(n-1)
def splice(s,n):
	return s[:n]+s[n+1:]
r = 1000000
tor = []
for i in range(10):
	n = 9-i
	f = fact(n)
	fr = r // f
	print(r,f,fr)
	r = r - fr * f
	print(r)
	tor.append(pp[fr])
	pp = splice(pp,fr)

print(tor)
