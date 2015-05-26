nums = '0123456789'
div = [2,3,5,7,11,13,17]
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def check(n):
	n = int(n)
	return 0 not in [(n // 10**(6-i))%1000%div[i]== 0 for i in range(len(div))]

ans = 0

for p in all_perms(nums):
	if check(p): ans += int(p)

print(ans)