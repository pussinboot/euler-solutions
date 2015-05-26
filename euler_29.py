ns = set()
for a in range(2,101):
	for b in range(2,101):
		ns.add(a**b)
print(len(ns))