#print(str(bin(256))[2:])
#print(str(bin(256))[2:][::-1])
total = 0
for i in range(1,1000001,2):
	if str(i) == str(i)[::-1]:
		if str(bin(i))[2:] == str(bin(i))[2:][::-1]:
			total += i
print(total)