def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n-1)

a = fact(100)
s = str(a)
total = 0
for i in range(len(s)):
	total += int(s[i])

print(total)