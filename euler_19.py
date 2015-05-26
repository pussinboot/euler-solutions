#month  -> days
# 1  2  3  4  5  6  7  8  9 10 11 12
#31  * 31 30 31 30 31 31 30 31 30 31
#* -> 28 or if year % 4 (but not if % 100 except % 400) 29

def days(mon,year):
	if mon == 2:
		if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0): return 28
		else: return 29
	elif mon < 9 and mon % 2 != 0: return 31
	elif mon == 10 or mon == 12: return 31
	else: return 30

count = 0
curr = 1
for i in range(1,13): # for 1900
	curr += days(i,1900)
if curr % 7 == 0: count += 1
for y in range(1901,2001):
	for m in range(1,13):
		curr += days(m,y)
		if curr % 7 == 0: count += 1

print(count)
	#print(y)

# 1200 / 7 :^)