
def sum_digits(n,p):
	r = 0
	while n:
		r, n = r + (n % 10)**p, n // 10
	return r

tor = 0
for i in range(10,6*9**5):
	if sum_digits(i,5) == i:
		tor += i
print(tor)