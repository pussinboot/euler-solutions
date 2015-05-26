f = open('p022_names.txt','r')
f = f.read()
f = f.split('","')
sort= sorted(f)
#print(sort)
#print(sort[0])
#print(ord(sort[0][1]))
#for i in range(26):
#	print(chr(65+i))
def wordval(word):
	tor = 0
	for c in word:
		tor += ord(c) - 64
	return tor
total = 0
for i in range(len(sort)):
	total += (i+1)*wordval(sort[i])

print(total)