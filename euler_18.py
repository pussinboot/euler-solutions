tree = ["75","95 64".split(" "),"17 47 82".split(" "),"18 35 87 10".split(" "),"20 04 82 47 65".split(" "),"19 01 23 75 03 34".split(" "),"88 02 77 73 07 63 67".split(" "),"99 65 04 28 06 16 70 92".split(" "),"41 41 26 56 83 40 80 70 33".split(" "),"41 48 72 33 47 32 37 16 94 29".split(" "),"53 71 44 65 25 43 91 52 97 51 14".split(" "),"70 11 33 28 77 73 17 78 39 68 17 57".split(" "),"91 71 52 38 17 14 91 43 58 50 27 29 48".split(" "),"63 66 04 68 89 53 67 30 73 16 69 87 40 31".split(" "),"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23".split(" ")]
#tree[0] = list(map(int, tree[0]))
mapped_data = [map(int,single_dimensional) for single_dimensional in tree]
newtree = []
for mapped_int in mapped_data:
	newtree.append(list(mapped_int))

newtree[0][0] = 79
newtree[0][1] = 0
#print(newtree)
#print(tree[1][1])
#tree[row][~col~]
# one step
#def node(r,c):
#	n = int(tree[r][c])
#	#print(n)
#	if r == 14: return n
#	else:
#		return n + max(node(r+1,c),node(r+1,c+1))
#
#print(node(0,0))

# two step
#def two_step(r,c):
#	if r == 13: return node(r,c)
#	n = int(tree[r][c])
#	lf = int(tree[r+1][c])
#	rt = int(tree[r+1][c+1])
#	ll = int(tree[r+2][c])
#	mm = int(tree[r+2][c+1])
#	rr = int(tree[r+2][c+2])
#	return n + max(two)

# bottom up
l = range(len(newtree)-1)
for i in l[::-1]:
	for j in range(len(newtree[i])-1):
		newtree[i][j] = newtree[i][j] + max(newtree[i+1][j],newtree[i+1][j+1])

print(newtree[0][0])