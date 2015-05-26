#1-20
#0, double, triple
#25 50
#
#last must be double
#just double
#double + 1d/s/t
#double + all sums of 2 d/s/t
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,25] 
d = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,50] 
t = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
def sumtwoless(aa,bb,dd):
	tor = 0
	for a in aa:
		for b in bb:
			if a + b < dd:
				tor += 1
	return tor

def sumtwoless_norep(aa,bb,dd):
	cc = []
	tor = 0
	for a in aa:
		for b in bb:
			if a + b < dd and (a,b) not in cc and (b,a) not in cc: 
				#print(a,b,dd)
				tor += 1
				cc.append((a,b))
	return tor

def sumtripless(aa,bb,cc,dd):
	tor = 0
	for a in aa:
		tor += sumtwoless_norep(bb,cc,dd-a)
	return tor

tor = len(d)
combo = [s,d,t]
for i in range(3):
	r1 = sumtwoless(d,combo[i],100)
	tor += r1
	for j in range(i,3):
		r2 = sumtripless(d,combo[i],combo[j],100)
		tor += r2

print(tor)
