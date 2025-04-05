def f(n, a, b):
    fib = [a, b]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
print(f(6, 2, 3))