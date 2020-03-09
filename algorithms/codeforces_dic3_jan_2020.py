# python 3.5.2

# generate all the primes,
# loop up to the sqrt
# find the first prime which divides the number
# recurse on that number to find the second prime (uniq) which divides num2
# c = n / a*b (c is uniq)


def find_next_divisor(n, blacklist=None):
    for i in range(2, sqrt(n)):
        if i == blacklist:
            continue
        if n % i == 0:
            return i


x = find_next_divisor(n)
if x is None:
    return 'NO'
y = find_next_divisor(n / x, x)
if y is None:
    return 'NO'
z = n / (x * y)
if z not in {x, y, 1}:
    return (x, y z)
return 'NO'


print("Hello, world!")
sl
