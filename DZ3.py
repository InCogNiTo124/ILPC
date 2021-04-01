import math
import operator as op

from functools import reduce


# Marko Josipović
def zad01(d):
    return {v: k for k, v in d.items()}

# Mario Ljubić
def rows_in_reverse(*args):
    return '\n'.join(map(lambda elem: str(elem), reversed(args)))

# Marko Josipović
def sum(args):
    return reduce(op.add, args)
def any(args):
    return reduce(op.or_, args)
def all(args):
    return reduce(op.and_, args)
def min(args):
    return reduce(lambda a,b: a if a<b else b, args)
def max(args):
    return reduce(lambda a,b: a if a>b else b, args)

# Marko Josipović
def zad04(num):
    def digits(num):
        while num > 0:
            num, digit = divmod(num, 10)
            yield digit
    return sum(digits(num))

# Mario Ljubić
def binomial_coeff(n, k):
    assert n>=0 and k>=0 and k<=n, 'Greška pri upisu'
    if k==0:
        return 1
    else:
        return int(reduce(op.mul, map(lambda i: (n+1-i)/i, range(1,k+1))))


# Marko Josipović
def zad06(n):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                return True
        return False
    
    def primes(num):
        for i in range(num):
            if is_prime(i):
                yield i

    def mapiranje(num):
        return 1-1/num
    
    return int(n * reduce(op.mul, map(mapiranje, \
        filter(lambda x: n%x==0, primes(n)))))


# Marko Josipović
def zad07(samples):
    #prepisan pseudokod
    M = 0
    S = 0
    for k in range(len(samples)):
        x = samples[k]
        oldM = M
        M = M + (x-M)/(k+1)
        S = S + (x-M)*(x-oldM)
        yield M, S/(k+1)

if __name__ == '__main__':
    #print(zad01({'a': 1, 'b':2, 'c': 3}))
    #print(zad02('mrmlj', 'sdgj', 'jkfadls', a='prvi'))

    #print(sum([1,2,4]))
    #print(any([True,True,True]))
    #print(all([True,True,True]))
    #print(min([544,19,7,9,14,56,8]))
    #print(max([1,5,2,7,4]))

    #print(zad04(2153121))
    #print(zad05(10,5)) #252
    #print(zad06(20))
    print(list(zad07([1,2,4])))
    
    
