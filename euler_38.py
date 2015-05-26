nums = '123456789'
def pandigital(str):
    """Check whether 'str' contains ALL of the chars in 'nums'"""
    return 0 not in [c in str for c in nums]

def multiples(num,n):
	tor = ""
	for i in range(1,n+1):
		tor += str(num*i)
	return tor

print(multiples(192,3))
print(pandigital(multiples(192,3)))

largest = 0
p = ""
n = 2
num = 0
going = True
while going:
	num += 1
	if n > 9:
			going = False
	p = multiples(num,n)
	if len(p) > 9:
		p = ""
		n += 1
		num = 1
	if(pandigital(p)):
		if int(p) > largest: largest = int(p)

print(largest)
