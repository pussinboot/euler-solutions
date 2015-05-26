from euler_lib import fact

def fact_digits(n):
	r = 0
	while n:
		r, n = r + fact(n % 10), n // 10
	return r
s = 0
for i in range(3,7*fact(9)+1):
	if i == fact_digits(i): s += i
#print(fact_digits(145))
print(s)