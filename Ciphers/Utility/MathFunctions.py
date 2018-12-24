def primes():
    D = {}
    q = 2
    while True:
        if q not in D:

            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

# This is an excessively simple way of finding all the factors btu we're only
# using it on very small numbers.
def factors(n):
    L = []
    for i in range(2,n):
        if n % i == 0:
            L.append(i)
    return L