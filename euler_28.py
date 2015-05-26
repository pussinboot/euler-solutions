#1 + [3,5,7,9] + [13,17,21,25]
def spiral_diag(n):
	tor = 1
	l = 1
	for i in range(1,(n-1)//2+1):
		for j in range(1,5):
			l += 2*i
			#print(l)
			tor += l
	return tor

print(spiral_diag(1001))