#1 2 3 4 5 6 7 8 9
#`````````````````
#3 3 5 4 4 3 5 5 4

#10 11 12 13 14 15 16 17 18 19 
#`````````````````````````````
# 3  6  6  8  8  7  7  9  8  8

#20 30 40 50 60 70 80 90
#```````````````````````
# 6  6  5  5  5  7  6  6

#and
#```
# 3

#100
#```
# 7
db = [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8,6,6,5,5,5,7,6,6]
def num_to_let(n):
	if n <= 0:
		return 0
	elif n < 21:
		return db[n-1]
	elif n < 100:
		return db[17+n//10] + num_to_let(n % 10)
	else:
		if n % 100 == 0:
			return db[n//100-1] + 7
		else:	
			return db[n//100-1] + 7 + 3 + num_to_let(n % 100)
print(num_to_let(342))
print(num_to_let(115))
tor = 11 # one thousand
for i in range(1000):
	tor += num_to_let(i)

print(tor)
#21124