def gen_triags():
    """ Generate an infinite sequence of triangular numbers.
    """
    last = 1
    new = 1  

    while True:
        yield new
        last += 1
        new += last
def divisor_gen(n):
    """quadratic sieve"""
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i is 0:
            yield i
            if i is not n / i:
                divisors.insert(0, n / i)
    for div in divisors:
        yield div

def divisors(n):
    return [d for d in divisor_gen(n)]

#def num_factors(n):
#    tor = 0
#    for i in range(1,n+1):
#        if n % i == 0: tor += 1
#    return tor
#for _ in range(7):
#    tt = next(t)
#    print(tt,num_factors(tt))

#n = 0
#while n < 500:
#    tt = next(t)
#    n = num_factors(tt)
#    #print(n)
#print("------------")
#print(tt)

t = gen_triags()
n = 0
while n < 500:
    tt = next(t)
    n = len(divisors(tt))

print(tt)