def coinsum(n,coins):
	ways = [0] * (n + 1)
	ways[0] = 1
	for coin in coins:
		for j in range(coin,n + 1):
			ways[j] += ways[j-coin]
	return ways[n]

print(coinsum(200,[1,2,5,10,20,50,100,200]))
coins = [1,2,5,10,20,50,100,200]
def coinsum_rec(n,i):
	if i <= 0: return 1
	res = 0
	while n >= 0:
		res = res + coinsum_rec(n,i-1)
		n = n - coins[i]
	return res
print(coinsum_rec(200,7))