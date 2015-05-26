sum = 0
ssum = 0
for i in range(1,101):
	sum += i
	ssum += i**2
print(sum**2-ssum)