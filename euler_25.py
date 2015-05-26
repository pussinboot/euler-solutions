def gen_fibb():
    """ Generate an infinite sequence of fibonacci numbers.
    """
    f1 = 0
    f2 = 0
    new = 1

    while True:
        yield new
        f1 = f2
        f2 = new
        new = f1 + f2

g = gen_fibb()
n = next(g)
i = 1
while len(str(n)) < 1000:
	i += 1
	n = next(g)

print(n)
print(i)
