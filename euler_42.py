def triangle_num(n):
	return n*(n+1)//2



f = open('p042_words.txt','r')
f = f.read()
f = f[1:-1].split('","')
#ml = 0
#for w in f:
#	if len(w) > ml: ml = len(w)
#print(ml)
#--> 14 * 26

tnums = []
n = 0
i = 1
while n < 14*26+2:
	n = triangle_num(i)
	tnums.append(n)
	i += 1
#print(tnums)
def wordval(word):
	tor = 0
	for c in word:
		tor += ord(c) - 64
	return tor
count = 0
for w in f:
	if wordval(w) in tnums: count += 1

print(count)