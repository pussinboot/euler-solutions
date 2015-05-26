sum = 0

for i in range(1,1001):
	n = i**i
	n = str(n)
	sum += int(n[-10:])

print(str(sum)[-10:])