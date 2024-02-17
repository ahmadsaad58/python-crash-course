# Fibonacci Sequence

# f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)

# Simple recursive
def fib(n):
    if n == 0:
        return 0
    if n ==  1:
        return 1

    return fib(n-1) + fib(n-2)

# print([fib(n) for n in range(15)])

# simple caching 
cache = {0: 0, 1: 1}

def fib_cached(n):
    if n in cache:
        return cache[n]

    cache[n] = fib_cached(n-1) + fib_cached(n-2)
    return cache[n]

# print([fib_cached(n) for n in range(100)])

# iterative no cache
def fib_iterative(n):
    if n in {0, 1}:
        return n

    fib_num, prev = 1, 0
    for _ in range(2, n+1):
         prev, fib_num = fib_num, prev + fib_num

    return fib_num

# print([fib_iterative(n) for n in range(100)])


# memoize with decorator 

def memoize(func):
    memo = {}

    def use_memo(n): 
        if n in memo:
            return memo[n]
        else: 
            memo[n] = func(n)
            return memo[n]
    
    return use_memo

@memoize
def fib_decorator(n):
    if n == 0:
        return 0
    if n ==  1:
        return 1

    return fib_decorator(n-1) + fib_decorator(n-2) 

print([fib_decorator(n) for n in range(100)])
