#odd composite numbers
#3 + 2*i not prime

#check isprime composite num - increasing squares, if > 0 and not prime u win
import euler_lib

def gen_odd_composites():
	n = 3
	while True:
		if not euler_lib.is_prime(n):
			yield n
		n += 2

oc = gen_odd_composites()

while True:
	n = next(oc)
	i = 1
	while not euler_lib.is_prime(n - 2*i**2):
		if n - 2*i**2 <= 0:
			print('answer found:',n)
			exit()
		i+=1
