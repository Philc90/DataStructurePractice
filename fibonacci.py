def fib(n):
    arr = []
    a, b = 0, 1
    for i in range(n):
        arr.append(a)
        a, b = b, a + b
    return arr

print(fib(10))