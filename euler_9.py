def check_pytrip(a,b,c):
	if a < b and a**2 + b**2 == c**2: return True
	return False

print(check_pytrip(3,4,5))

for a in range(1001):
	for b in range(1001):
		if b > a:
			c = 1000 - a - b
			if c > b: 
				if check_pytrip(a,b,c): print([a,b,c])
				
# smart math way doesnt work lol
#for m in range(1,501):
#	n = 500/m - m
#	if m > n:
#		a = m**2 - n**2
#		b = 2 * m * n
#		c = m**2 + n**2
#		if check_pytrip(a,b,c): print([a,b,c])