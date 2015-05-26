coins = [1,2,3,4]
def coinsum_rec(n,i):
	if i <= 0: return 1
	res = 0
	while n >= 0:
		res = res + coinsum_rec(n,i-1)
		n = n - coins[i]
	return res
print(coinsum_rec(5,3))
#but also needs permutations -///-