from functools import reduce
# Find Fibonacci series for given length using lambda and reduce function
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
## generating fibonnacci number
print(fib(3))
print(fib(4))
print(fib(8))
