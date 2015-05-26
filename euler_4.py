
def pals(nd):
	toReturn = []
	for a in range(10**(nd-1),10**nd):
		for b in range(10**(nd-1),10**nd):
			temp = a*b
			if str(temp) == str(temp)[::-1]:
				toReturn.append(temp)
	return toReturn

print(max(pals(3)))