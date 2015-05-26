def check(n,d):
	a = n/d
	n1, n2 = n // 10, n % 10
	d1, d2 = d // 10, d % 10
	if n2 == d2 and n2 != 0:
		if n1/d1 == a: return [(n,d),(n1,d1)]
	elif n2 == d1 and d2 != 0:
		if n1/d2 == a: return [(n,d),(n1,d2)]
	elif n1 == d2:
		if n2/d1 == a: return [(n,d),(n2,d1)]
	elif n1 == d1 and d2 != 0:
		if n2/d2 == a: return [(n,d),(n2,d2)]
	return []
tor = []
for n in range(10,100):
	for d in range(n+1,100):
		t = check(n,d)
		if t != []:
			tor.append(t)

print(tor)
1/4 * 1/5 * 2/5 * 4/8
